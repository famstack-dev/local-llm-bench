#!/usr/bin/env python3
"""
LLM inference benchmark for local models.

WHAT THIS DOES:
  Runs a multi-turn conversation scenario against a local LLM backend and
  measures two things per turn:
    1. TTFT (Time To First Token) — how long before the first word appears
    2. Generation speed — how fast the response streams out

  Most LLM UIs only show generation speed (tok/s). This benchmark shows
  that TTFT often dominates total response time, especially as conversation
  context grows. See docs/paper.md for the full analysis.

HOW IT WORKS:
  1. Loads a scenario JSON file (e.g. scenarios/agent.json) that defines
     a system prompt and a sequence of conversation turns with tool calls.
  2. For each turn, sends the accumulated message history to the model
     and streams the response, measuring TTFT and generation time.
  3. Appends the model's response to the history for the next turn,
     so context grows naturally — just like a real conversation.
  4. Saves all metrics to a JSON file for later comparison.

USAGE:
  # Run against Ollama (default backend)
  python3 bench.py --model qwen3.5:35b-a3b --label "Ollama GGUF"

  # Run against LM Studio
  python3 bench.py --backend lmstudio --model mlx-community/qwen3.5-35b-a3b --label "LM Studio MLX"

  # Run against raw llama-server (llama.cpp without Ollama wrapper)
  python3 bench.py --backend llama-server --base-url http://localhost:8090 --model qwen3.5:35b-a3b --label "llama-server"

  # Run twice to compare cold vs warm cache
  python3 bench.py --model qwen3.5:35b-a3b --label "Ollama" --runs 2

  # Compare results from multiple runs
  python3 compare.py results/agent_ollama_gguf.json results/agent_lmstudio_mlx.json

REQUIREMENTS:
  - Python 3.8+ (stdlib only, no pip install needed)
  - A running inference backend (Ollama, LM Studio, or llama-server)
  - The model loaded in that backend
"""

import argparse
import json
import os
import subprocess
import sys
import time
import urllib.request
import urllib.error

# Add the repo root to the import path so we can import from lib/
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from lib.backends import get_backend, get_model_info, DEFAULT_URLS
from lib.output import save_results, make_result_path, make_chip_slug, print_turn_header, print_turn_row, print_summary


# ── Install instructions shown when a backend isn't reachable ────────
# These help messages tell the user exactly what to do to fix the problem.
INSTALL_HINTS = {
    "ollama": (
        "Ollama is not running at {url}.\n"
        "\n"
        "  To fix:\n"
        "    1. Install:  brew install ollama\n"
        "    2. Start:    brew services start ollama\n"
        "    3. Pull:     ollama pull {model}\n"
        "    4. Verify:   curl {url}/api/tags\n"
        "\n"
        "  Or use --base-url to point to a different Ollama instance."
    ),
    "lmstudio": (
        "LM Studio is not running at {url}.\n"
        "\n"
        "  To fix:\n"
        "    1. Download LM Studio from https://lmstudio.ai/\n"
        "    2. Open it and load a model\n"
        "    3. Start the local server (Developer tab → Start Server)\n"
        "    4. Verify:   curl {url}/v1/models\n"
        "\n"
        "  Or use --base-url to point to a different LM Studio instance."
    ),
    "llama-server": (
        "llama-server is not running at {url}.\n"
        "\n"
        "  To fix:\n"
        "    1. Build llama.cpp: https://github.com/ggml-org/llama.cpp\n"
        "    2. Start:   ./llama-server -m model.gguf --port 8090\n"
        "    3. Verify:  curl {url}/v1/models\n"
        "\n"
        "  Or use --base-url to point to a different llama-server instance."
    ),
    "minimax": (
        "MiniMax API is not accessible at {url}.\n"
        "\n"
        "  To fix:\n"
        "    1. Get an API key at https://platform.minimax.io/\n"
        "    2. Set:     export MINIMAX_API_KEY=your-key-here\n"
        "    3. Verify:  curl -H 'Authorization: Bearer $MINIMAX_API_KEY' {url}/v1/models\n"
        "\n"
        "  Models: MiniMax-M2.5, MiniMax-M2.5-highspeed"
    ),
}


def check_backend(backend, base_url, model):
    """
    Verify that the inference backend is reachable and the model is available.

    Two checks:
    1. Is the backend running? (HTTP health check)
    2. Is the requested model loaded/available? (Ollama: /api/tags, LM Studio: /v1/models)

    Fails fast with a clear message and the exact command to fix the problem.
    """
    # ── Check 1: Is the backend reachable? ────────────────────────────
    # Cloud backends (MiniMax) don't expose a /v1/models endpoint.
    # We just verify the API key is set — the streaming call will fail
    # with a clear error if the key is invalid.
    if backend == "minimax":
        api_key = os.environ.get("MINIMAX_API_KEY", "")
        if not api_key:
            print("Error: MINIMAX_API_KEY environment variable is required.\n"
                  "  Get your key at https://platform.minimax.io/", file=sys.stderr)
            sys.exit(1)
        return  # Skip HTTP health check for cloud backends

    if backend == "ollama":
        check_url = f"{base_url}/api/tags"
    else:
        check_url = f"{base_url}/v1/models"

    try:
        req = urllib.request.Request(check_url)
        resp = urllib.request.urlopen(req, timeout=10)
        body = resp.read()
    except (urllib.error.URLError, OSError) as e:
        hint = INSTALL_HINTS[backend].format(url=base_url, model=model)
        print(f"Error: {hint}", file=sys.stderr)
        sys.exit(1)

    # ── Check 2: Is the model available? ──────────────────────────────
    if backend == "ollama":
        try:
            data = json.loads(body)
            available = [m.get("name", "") for m in data.get("models", [])]
            # Ollama model names can be "llama3.1:8b" or "llama3.1:latest"
            # Match on the base name (before :) if no exact match
            model_base = model.split(":")[0]
            found = any(
                m == model or m.startswith(model_base + ":")
                for m in available
            )
            if not found:
                print(f"Error: Model '{model}' is not available in Ollama.\n", file=sys.stderr)
                if available:
                    print(f"  Available models:", file=sys.stderr)
                    for m in sorted(available):
                        print(f"    - {m}", file=sys.stderr)
                print(f"\n  To download it:\n    ollama pull {model}\n", file=sys.stderr)
                sys.exit(1)
        except (json.JSONDecodeError, KeyError):
            pass  # Can't parse response, let the benchmark try anyway


def warm_up(stream_fn, base_url, model, backend):
    """
    Send a short throwaway request to ensure the model is loaded into memory.

    WHY THIS MATTERS:
      Ollama (and some other backends) load models on demand and unload them
      after an idle timeout (default: 5 minutes). If the model isn't loaded,
      Turn 1 TTFT includes model loading time (10-20s for a 35B model) which
      has nothing to do with prefill speed.

      By sending a trivial "hi" message first, we force the model into memory
      so Turn 1 measures actual prefill performance. The warm-up response is
      discarded — it's not part of the benchmark.

      Use --cold to skip this and include model loading time in the results.
    """
    print("  Warming up (loading model into memory)...", end="", flush=True)
    try:
        t_start = time.time()
        messages = [{"role": "user", "content": "hi"}]
        stream_fn(base_url, model, messages, max_tokens=1, temperature=0)
        warm_up_time = time.time() - t_start
        print(f" ready ({warm_up_time:.1f}s).\n")
        return round(warm_up_time, 3)
    except Exception as e:
        print(f" failed: {e}", file=sys.stderr)
        print(f"  Check that '{model}' is available in {backend}.", file=sys.stderr)
        sys.exit(1)


def load_scenario(path):
    """
    Load a scenario from a JSON file.

    A scenario defines:
    - system_prompt: the system message sent with every request
    - turns: a list of conversation turns, each with:
      - user: the user's message
      - tool: (optional) which tool the assistant calls
      - tool_result: (optional) the tool's output (JSON or text)
    - max_tokens: output token limit per turn
    - temperature: sampling temperature

    See scenarios/agent.json for an example.
    """
    if not os.path.exists(path):
        # List available scenarios to help the user pick one
        script_dir = os.path.dirname(os.path.abspath(__file__))
        scenario_dir = os.path.join(script_dir, "scenarios")
        available = []
        if os.path.isdir(scenario_dir):
            available = [f for f in os.listdir(scenario_dir) if f.endswith(".json")]
        msg = f"Error: Scenario file not found: {path}\n"
        if available:
            msg += f"\n  Available scenarios in scenarios/:\n"
            for s in sorted(available):
                msg += f"    - {s}\n"
            msg += f"\n  Usage: python3 bench.py --scenario scenarios/{available[0]} --model MODEL --label LABEL"
        print(msg, file=sys.stderr)
        sys.exit(1)

    with open(path) as f:
        try:
            return json.load(f)
        except json.JSONDecodeError as e:
            print(f"Error: Invalid JSON in scenario file {path}: {e}", file=sys.stderr)
            sys.exit(1)


def run_scenario(scenario, stream_fn, base_url, model, runs=1, backend="ollama"):
    """
    Run a benchmark scenario and collect metrics per turn.

    TWO MODES (set via "mode" in the scenario JSON):

      "conversation" (default):
        Messages accumulate across turns, just like a real chat.
        Context grows with every turn, revealing the prefill bottleneck.

        Turn 1: [system, user1, tool_call, tool_result] → model responds
        Turn 2: [system, user1, ..., assistant1, user2, ...] → model responds

      "single-shot":
        Each turn starts fresh with only the system prompt.
        Context stays roughly constant. Tests raw prefill + generation
        without context accumulation — useful for classification, summary,
        and other stateless tasks.

        Turn 1: [system, user1] → model responds
        Turn 2: [system, user2] → model responds  (Turn 1 is gone)

    CONTEXT ESTIMATION:
      We estimate token count as character_count / 4. This is rough but
      consistent across runs, making relative comparisons valid.
    """
    all_results = []
    mode = scenario.get("mode", "conversation")

    for run in range(1, runs + 1):
        # Start each run with a fresh message history
        system_msg = {"role": "system", "content": scenario["system_prompt"]}
        messages = [system_msg]
        results = []
        max_tokens = scenario.get("max_tokens", 500)
        temperature = scenario.get("temperature", 0.6)

        # Print run header
        mode_label = "single-shot" if mode == "single-shot" else "conversation"
        print(f"\n{'='*85}")
        print(f"  {scenario['name'].upper()} BENCHMARK — {model} — Run {run}")
        print(f"  Backend: {backend} @ {base_url}")
        print(f"  {len(scenario['turns'])} turns, max_tokens={max_tokens}, mode={mode_label}")
        print(f"{'='*85}\n")
        print_turn_header(backend)

        # Track previous context size to calculate "new tokens" per turn
        prev_ctx_chars = len(scenario["system_prompt"])

        for i, turn in enumerate(scenario["turns"]):
            # ── In single-shot mode, reset to just the system prompt ──
            # Each turn is independent — no conversation history carried over.
            if mode == "single-shot":
                messages = [system_msg]
                prev_ctx_chars = len(scenario["system_prompt"])

            # ── Build messages for this turn ──────────────────────────
            # 1. Add the user's question
            messages.append({"role": "user", "content": turn["user"]})

            # 2. If there's a tool call, add the assistant's tool invocation
            #    and the tool's result as messages. This simulates the
            #    assistant-calls-tool pattern common in agent applications.
            tool = turn.get("tool")
            if tool:
                messages.append({"role": "assistant", "content": f"Let me run `{tool}` for you."})
                messages.append({"role": "user", "content": f"Tool `{tool}` returned:\n\n{turn['tool_result']}"})

            # ── Calculate context metrics ─────────────────────────────
            # How many tokens are in the full message history?
            ctx_chars = sum(len(m["content"]) for m in messages)
            ctx_tokens_est = ctx_chars // 4       # Rough estimate: 1 token ≈ 4 chars
            new_tokens_est = (ctx_chars - prev_ctx_chars) // 4  # New tokens added this turn

            try:
                # ── Send to model and measure ─────────────────────────
                # The stream function handles the HTTP request, streams
                # the response, and returns timing metrics.
                metrics = stream_fn(
                    base_url, model, messages,
                    max_tokens=max_tokens, temperature=temperature,
                )

                # ── Append model response to history ──────────────────
                # The model's response becomes part of the context for
                # the next turn. This is why context grows every turn.
                messages.append({"role": "assistant", "content": metrics["response"]})
                prev_ctx_chars = sum(len(m["content"]) for m in messages)

                # ── Build result record ───────────────────────────────
                result = {
                    "turn": i + 1,
                    "run": run,
                    "ctx_tokens_est": ctx_tokens_est,
                    "new_tokens_est": new_tokens_est,
                    "ttft": round(metrics["ttft"], 3),
                    "gen_time": round(metrics["gen_time"], 3),
                    "gen_tps": round(metrics["gen_tps"], 1),
                    "total": round(metrics["total"], 3),
                    "output_tokens": metrics["output_tokens"],
                }
                if tool:
                    result["tool"] = tool
                # Include Ollama-specific eval stats if available
                if metrics.get("prompt_eval_count") is not None:
                    result["prompt_eval_count"] = metrics["prompt_eval_count"]
                if metrics.get("prompt_eval_duration_ms"):
                    result["prompt_eval_duration_ms"] = round(metrics["prompt_eval_duration_ms"], 1)

                print_turn_row(result, backend)
                results.append(result)

            except Exception as e:
                # Record errors but keep going — one failed turn shouldn't
                # abort the whole benchmark
                print(f"{i+1:>4}  ERROR: {e}")
                messages.append({"role": "assistant", "content": "Error processing request."})
                prev_ctx_chars = sum(len(m["content"]) for m in messages)
                results.append({"turn": i + 1, "run": run, "error": str(e)})

        # Print run summary
        print()
        print_summary(results, f"Run {run}:")
        all_results.extend(results)

    return all_results


def find_all_scenarios(script_dir):
    """Find all scenario JSON files in the scenarios/ directory."""
    scenario_dir = os.path.join(script_dir, "scenarios")
    if not os.path.isdir(scenario_dir):
        return []
    paths = sorted(
        os.path.join(scenario_dir, f)
        for f in os.listdir(scenario_dir)
        if f.endswith(".json")
    )
    return paths


def run_single(args, scenario_path, script_dir, stream_fn, base_url, warm_up_done):
    """
    Run a single scenario benchmark and save results.

    Returns the warm_up_time (so we only warm up once for --all).
    """
    scenario = load_scenario(scenario_path)

    # Warm up once (first scenario only)
    warm_up_time = None
    if not args.cold and not warm_up_done:
        warm_up_time = warm_up(stream_fn, base_url, args.model, args.backend)

    results = run_scenario(
        scenario, stream_fn, base_url, args.model,
        runs=args.runs, backend=args.backend,
    )

    # Don't save if every turn failed
    valid = [r for r in results if "error" not in r]
    if not valid:
        print(f"\nError: All {len(results)} turns failed for {scenario['name']}. Skipping.", file=sys.stderr)
        return warm_up_time

    # Save results
    label = args.label or f"{make_chip_slug()} {args.backend}"
    outpath = args.output or make_result_path(script_dir, args.model, scenario["name"], args.backend)
    os.makedirs(os.path.dirname(outpath), exist_ok=True)
    meta = {
        "scenario": scenario["name"],
        "mode": scenario.get("mode", "conversation"),
        "label": label,
        "backend": args.backend,
        "model_info": get_model_info(args.backend, base_url, args.model),
        "runs": args.runs,
        "max_tokens": scenario.get("max_tokens", 500),
        "cold": args.cold,
    }
    if warm_up_time is not None:
        meta["warm_up_time"] = warm_up_time
    save_results(outpath, meta, results)
    md_path = outpath.rsplit(".", 1)[0] + ".md"
    print(f"\n  JSON: {outpath}")
    print(f"  Table: {md_path}")
    return warm_up_time


def main():
    parser = argparse.ArgumentParser(
        description="LLM inference benchmark — measures TTFT + generation speed per turn"
    )
    parser.add_argument("--scenario", default=None,
                        help="Run a single scenario JSON file. Default: runs ALL scenarios.")
    parser.add_argument("--backend", choices=["ollama", "lmstudio", "llama-server", "minimax"],
                        default="ollama", help="Inference backend (default: ollama)")
    parser.add_argument("--base-url", default=None,
                        help="Override backend URL (default: auto from backend)")
    parser.add_argument("--model", default=None,
                        help="Model name/identifier as known by the backend")
    parser.add_argument("--label", default=None,
                        help="Human-readable label (default: auto-generated from hardware + backend)")
    parser.add_argument("--runs", type=int, default=1,
                        help="Consecutive runs (default: 1). Use 2+ to test warm cache vs cold.")
    parser.add_argument("--cold", action="store_true",
                        help="Skip warm-up request (include model loading time in Turn 1)")
    parser.add_argument("--output", default=None,
                        help="Output JSON path (default: auto-generated). Only used with --scenario.")
    parser.add_argument("--flash-attention", action="store_true",
                        help="Enable OLLAMA_FLASH_ATTENTION before running (sets env, restarts Ollama)")
    parser.add_argument("--kv-cache", default=None, metavar="TYPE",
                        help="Set OLLAMA_KV_CACHE_TYPE before running (e.g. q4_0, q8_0). Restarts Ollama.")
    parser.add_argument("--stock", action="store_true",
                        help="Clear all Ollama tuning flags and restart before running.")
    parser.add_argument("--check", action="store_true",
                        help="Show detected hardware and tuning flags, then exit.")
    args = parser.parse_args()

    # ── Apply or clear Ollama tuning flags ────────────────────────────
    if args.stock or args.flash_attention or args.kv_cache:
        from lib.output import _get_ollama_env
        changed = False

        if args.stock:
            # Clear everything
            for key in ["OLLAMA_FLASH_ATTENTION", "OLLAMA_KV_CACHE_TYPE"]:
                if _get_ollama_env(key):
                    subprocess.run(["launchctl", "unsetenv", key], check=False)
                    os.environ.pop(key, None)
                    changed = True
            if changed:
                print("  Cleared Ollama tuning flags.")
        else:
            if args.flash_attention:
                subprocess.run(["launchctl", "setenv", "OLLAMA_FLASH_ATTENTION", "1"], check=True)
                os.environ["OLLAMA_FLASH_ATTENTION"] = "1"
                changed = True
            else:
                # Explicitly unset if not requested
                if _get_ollama_env("OLLAMA_FLASH_ATTENTION"):
                    subprocess.run(["launchctl", "unsetenv", "OLLAMA_FLASH_ATTENTION"], check=False)
                    os.environ.pop("OLLAMA_FLASH_ATTENTION", None)
                    changed = True

            if args.kv_cache:
                subprocess.run(["launchctl", "setenv", "OLLAMA_KV_CACHE_TYPE", args.kv_cache], check=True)
                os.environ["OLLAMA_KV_CACHE_TYPE"] = args.kv_cache
                changed = True
            else:
                if _get_ollama_env("OLLAMA_KV_CACHE_TYPE"):
                    subprocess.run(["launchctl", "unsetenv", "OLLAMA_KV_CACHE_TYPE"], check=False)
                    os.environ.pop("OLLAMA_KV_CACHE_TYPE", None)
                    changed = True

        if changed:
            print("  Restarting Ollama...", end=" ", flush=True)
            subprocess.run(["brew", "services", "restart", "ollama"],
                           capture_output=True, check=True)
            import time as _time
            _time.sleep(3)
            print("done.")

    def print_config():
        from lib.output import get_system_info, make_chip_slug, make_config_suffix
        info = get_system_info()
        suffix = make_config_suffix()
        ollama = info.get("ollama", {})
        fa = ollama.get("flash_attention")
        kv = ollama.get("kv_cache_type")
        wired = info.get("gpu_wired_limit_mb", 0)
        print(f"\n  Hardware:        {info.get('chip', '?')} / {info.get('memory_gb', '?')}GB / {info.get('gpu_cores', '?')} GPU cores")
        print(f"  Slug:            {make_chip_slug(info)}")
        print(f"  Flash attention: {'ON' if fa else 'off'}")
        print(f"  KV cache type:   {kv if kv else 'f16 (default)'}")
        print(f"  GPU wired limit: {str(wired) + ' MB' if wired else 'default'}")
        print(f"  Config suffix:   {'_' + suffix if suffix else '(none)'}")
        print()

    if args.check:
        print_config()
        sys.exit(0)

    if not args.model:
        parser.error("--model is required (e.g. --model llama3.1:8b)")

    print_config()

    # Resolve backend URL (use default if not specified)
    base_url = args.base_url or DEFAULT_URLS[args.backend]

    # Get the appropriate streaming function for this backend
    stream_fn = get_backend(args.backend)

    script_dir = os.path.dirname(os.path.abspath(__file__))

    # ── Pre-flight check ─────────────────────────────────────────────
    check_backend(args.backend, base_url, args.model)

    if args.scenario:
        # Run a single scenario
        scenario_path = args.scenario if os.path.isabs(args.scenario) else os.path.join(script_dir, args.scenario)
        run_single(args, scenario_path, script_dir, stream_fn, base_url, warm_up_done=False)
    else:
        # Default: run all scenarios
        scenarios = find_all_scenarios(script_dir)
        if not scenarios:
            print("Error: No scenario files found in scenarios/", file=sys.stderr)
            sys.exit(1)
        total = len(scenarios)
        print(f"\n  Running all {total} scenarios...\n")
        warm_up_done = False
        for i, scenario_path in enumerate(scenarios, 1):
            name = os.path.basename(scenario_path).replace(".json", "")
            print(f"\n  [{i}/{total}] {name}")
            warm_up_time = run_single(args, scenario_path, script_dir, stream_fn, base_url, warm_up_done)
            if warm_up_time is not None:
                warm_up_done = True
        print(f"\n  All {total} scenarios complete.")

        # ── Contribute prompt ─────────────────────────────────────────
        chip_slug = make_chip_slug()
        model_slug = make_result_path(script_dir, args.model, "", args.backend).split("/results/")[1].split("/")[0]
        branch = f"results/{chip_slug}"

        # Detect if this is a direct clone (no push access) or a fork
        is_fork = False
        try:
            remote_url = subprocess.check_output(
                ["git", "remote", "get-url", "origin"],
                stderr=subprocess.DEVNULL, cwd=script_dir,
            ).decode().strip()
            is_fork = "famstack-dev/local-llm-bench" not in remote_url
        except (subprocess.SubprocessError, FileNotFoundError):
            pass

        print(f"\n{'='*70}")
        print(f"\n  Want to contribute your results?\n")

        if not is_fork:
            print(f"  You cloned the repo directly. Fork it first:\n")
            print(f"  gh repo fork famstack-dev/local-llm-bench --clone=false")
            print(f"  git remote set-url origin https://github.com/<you>/local-llm-bench.git\n")

        print(f"  Then commit and open a PR:\n")
        print(f"  git checkout -b {branch}")
        print(f"  git add results/")
        print(f"  git commit -m \"results: {chip_slug} {args.backend} {model_slug}\"")
        print(f"  git push -u origin {branch}")
        print(f"  gh pr create --title \"results: {chip_slug}\" \\")
        print(f"    --body \"Benchmark results from {chip_slug} using {args.backend}\"")
        print(f"\n  Your numbers will be added to the comparison table at")
        print(f"  https://famstack.dev/guides/mlx-vs-gguf-apple-silicon")
        print(f"\n{'='*70}\n")


if __name__ == "__main__":
    main()
