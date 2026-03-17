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
  1. Loads a scenario JSON file (e.g. scenarios/ops-agent.json) that defines
     a system prompt and a sequence of conversation turns with tool calls.
  2. For each turn, sends the accumulated message history to the model
     and streams the response, measuring TTFT and generation time.
  3. Appends the model's response to the history for the next turn,
     so context grows naturally — just like a real conversation.
  4. Saves all metrics to a JSON file for later comparison.

USAGE:
  # Run against Ollama (default backend)
  python3 bench.py --model qwen3.5:35b-a3b --label "Ollama GGUF"

  # Run against LM Studio (--no-think disables Qwen3.5 thinking, restores template when done)
  python3 bench.py --backend lmstudio --model mlx-community/qwen3.5-35b-a3b --label "LM Studio MLX" --no-think

  # Run against raw llama-server (llama.cpp without Ollama wrapper)
  python3 bench.py --backend llama-server --base-url http://localhost:8090 --model qwen3.5:35b-a3b --label "llama-server"

  # Run against any OpenAI-compatible endpoint (vLLM, TGI, LocalAI, etc.)
  python3 bench.py --backend openai --base-url http://localhost:8000 --model my-model --label "vLLM"

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
import shutil
import signal
import subprocess
import sys
import time
import urllib.request
import urllib.error

# Add the repo root to the import path so we can import from lib/
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from lib.backends import get_backend, get_model_info, DEFAULT_URLS
from lib.output import save_results, make_result_path, make_model_slug, make_chip_slug, print_turn_header, print_turn_row, print_summary


# ── Thinking mode management for Qwen3.5 ─────────────────────────────
# Qwen3.5 defaults to thinking enabled. The chat template injects a
# <think> block that the model fills with hidden reasoning, burning tokens
# and distorting benchmarks. Disabling it requires patching the template.
#
# Model directories per backend:
#   LM Studio: ~/.lmstudio/models/<model>/chat_template.jinja
#   oMLX:      ~/.omlx/models/<model>/chat_template.jinja
MODEL_DIRS = {
    "lmstudio": os.path.expanduser("~/.lmstudio/models"),
    "openai":   os.path.expanduser("~/.omlx/models"),
}
THINK_OFF_LINE = "    {{- '<think>\\n\\n</think>\\n\\n' }}"
THINK_ON_TAIL = """{%- if add_generation_prompt %}
    {{- '<|im_start|>assistant\\n' }}
{%- endif %}"""
THINK_OFF_TAIL = """{%- if add_generation_prompt %}
    {{- '<|im_start|>assistant\\n' }}
    {{- '<think>\\n\\n</think>\\n\\n' }}
{%- endif %}"""


def find_chat_template(backend, model):
    """
    Resolve the chat_template.jinja path for a given backend and model.

    Models are stored as:
      <model_dir>/<model>/chat_template.jinja

    where <model> is the --model value (e.g. mlx-community/Qwen3.5-35B-A3B-4bit).
    """
    model_dir = MODEL_DIRS.get(backend)
    if not model_dir:
        return None
    template = os.path.join(model_dir, model, "chat_template.jinja")
    if os.path.exists(template):
        return template
    return None


def _thinking_is_off(template_path):
    """Check if the template already has thinking disabled."""
    with open(template_path) as f:
        return THINK_OFF_LINE in f.read()


def disable_thinking(template_path):
    """
    Back up the chat template and patch it to disable thinking.

    Returns the backup path, or None if thinking was already off.
    """
    if not os.path.exists(template_path):
        print(f"  Warning: --no-think ignored, template not found: {template_path}", file=sys.stderr)
        return None

    if _thinking_is_off(template_path):
        print("  Thinking is already OFF in the template.")
        return None

    # Back up the original — this is the file we MUST restore
    backup_path = template_path + ".bench-backup"
    shutil.copy2(template_path, backup_path)

    # Patch: inject pre-closed <think> block
    text = open(template_path).read()
    text = text.replace(THINK_ON_TAIL, THINK_OFF_TAIL)
    with open(template_path, "w") as f:
        f.write(text)

    # Verify
    if not _thinking_is_off(template_path):
        # Restore immediately if patch failed
        shutil.copy2(backup_path, template_path)
        os.remove(backup_path)
        print("  Error: Failed to patch thinking template.", file=sys.stderr)
        sys.exit(1)

    print("  Thinking disabled in template (backup saved).")
    return backup_path


def restore_thinking(template_path, backup_path):
    """Restore the original chat template from backup."""
    if backup_path and os.path.exists(backup_path):
        shutil.copy2(backup_path, template_path)
        os.remove(backup_path)
        print("\n  Template restored to original state.")


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
    "openai": (
        "OpenAI-compatible endpoint is not running at {url}.\n"
        "\n"
        "  This backend works with any server that implements the OpenAI API:\n"
        "    vLLM, text-generation-inference, LocalAI, LiteLLM, etc.\n"
        "\n"
        "  To fix:\n"
        "    1. Start your inference server\n"
        "    2. Verify:  curl {url}/v1/models\n"
        "    3. If auth is required:  export OPENAI_API_KEY=your-key-here\n"
        "\n"
        "  Use --base-url to point to a different host/port."
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
        # Pass API key for openai backend if set
        if backend == "openai":
            api_key = os.environ.get("OPENAI_API_KEY", "")
            if api_key:
                req.add_header("Authorization", f"Bearer {api_key}")
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


def estimate_max_context(scenario):
    """
    Estimate the maximum context tokens a scenario will need.

    For conversation mode, we sum all messages (context accumulates).
    For single-shot mode, we find the largest individual turn.
    Returns (max_tokens_est, max_tokens_output) tuple.
    """
    system_chars = len(scenario["system_prompt"])
    max_tokens = scenario.get("max_tokens", 500)
    mode = scenario.get("mode", "conversation")

    if mode == "single-shot":
        # Each turn is independent — find the largest one
        max_turn_chars = 0
        for turn in scenario["turns"]:
            turn_chars = len(turn["user"])
            if turn.get("tool_result"):
                turn_chars += len(turn["tool_result"]) + 50  # tool overhead
            max_turn_chars = max(max_turn_chars, turn_chars)
        return (system_chars + max_turn_chars) // 4, max_tokens
    else:
        # Conversation mode — all messages accumulate
        total_chars = system_chars
        for turn in scenario["turns"]:
            total_chars += len(turn["user"])
            if turn.get("tool_result"):
                total_chars += len(turn["tool_result"]) + 50
            total_chars += max_tokens * 4  # estimate assistant reply length
        return total_chars // 4, max_tokens


def check_context_size(stream_fn, base_url, model, backend, needed_tokens):
    """
    Verify the backend's context window is large enough for the benchmark.

    Sends a test request padded to the required context size and checks if
    the model can produce output. Fails fast with clear instructions if not.
    """
    # Pad a system prompt to approximate the needed context size
    # Each "word " is ~1.25 tokens, so we need roughly needed_tokens * 4 chars
    padding_chars = max(0, needed_tokens * 4 - 100)
    padding = "test " * (padding_chars // 5)
    messages = [
        {"role": "system", "content": padding},
        {"role": "user", "content": "Reply with the single word OK."},
    ]

    print(f"  Checking context window ({needed_tokens:,} tokens needed)...", end="", flush=True)
    try:
        metrics = stream_fn(base_url, model, messages, max_tokens=5, temperature=0)
        if metrics["output_tokens"] == 0:
            _print_context_error(needed_tokens, backend)
        print(" ok.\n")
    except Exception as e:
        err = str(e).lower()
        if any(k in err for k in ["context", "too long", "exceed", "length", "413", "400"]):
            _print_context_error(needed_tokens, backend)
        # Other errors (network, auth) — let the benchmark handle them
        print(f" skipped ({e}).\n")


def _print_context_error(needed_tokens, backend):
    """Print a clear error message about insufficient context window."""
    print(f"\n\n{'='*70}")
    print(f"\n  Error: Context window is too small for the benchmark.")
    print(f"  The scenarios need at least ~{needed_tokens:,} tokens of context.")
    print(f"  Recommendation: set your context window to at least 16,384 tokens.\n")

    hints = {
        "ollama": "  Ollama: create a Modelfile with PARAMETER num_ctx 16384",
        "lmstudio": "  LM Studio: change Context Length in the model settings UI",
        "openai": "  oMLX: admin panel -> Settings -> Generation Defaults -> Max Context Window\n"
                  "  Other: check your server's context/max_seq_len setting",
        "llama-server": "  llama-server: restart with -c 16384",
    }
    print(hints.get(backend, "  Check your backend's context window setting."))
    print(f"\n  After changing the setting, reload the model in your backend")
    print(f"  for the new context size to take effect.")
    print(f"\n  Full guide: docs/setup-guide.md")
    print(f"\n{'='*70}\n")
    sys.exit(1)


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

                # ── Check for empty output (likely context too small) ──
                if metrics["output_tokens"] == 0:
                    print(f"\n  Turn {i+1} produced 0 output tokens.")
                    _print_context_error(ctx_tokens_est + max_tokens, backend)

                # Save response text for quality comparison (not in JSON metrics)
                result["_response"] = metrics["response"]
                result["_user"] = turn["user"]

                print_turn_row(result, backend)
                results.append(result)

            except Exception as e:
                print(f"\n  Benchmark aborted at turn {i+1} (~{ctx_tokens_est:,} tokens context).")
                print(f"  Error: {e}")
                print(f"\n  If this is a context size issue, see docs/setup-guide.md")
                sys.exit(1)

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
    backend_key = args.backend_label or args.backend

    # Warm up once (first scenario only)
    warm_up_time = None
    if not args.cold and not warm_up_done:
        warm_up_time = warm_up(stream_fn, base_url, args.model, args.backend)

    results = run_scenario(
        scenario, stream_fn, base_url, args.model,
        runs=args.runs, backend=backend_key,
    )

    # Don't save if every turn failed
    valid = [r for r in results if "error" not in r]
    if not valid:
        print(f"\nError: All {len(results)} turns failed for {scenario['name']}. Skipping.", file=sys.stderr)
        return warm_up_time

    # Save results
    label = args.label or f"{make_chip_slug()} {backend_key}"
    outpath = args.output or make_result_path(script_dir, args.model, scenario["name"], backend_key)
    os.makedirs(os.path.dirname(outpath), exist_ok=True)
    meta = {
        "scenario": scenario["name"],
        "mode": scenario.get("mode", "conversation"),
        "label": label,
        "backend": backend_key,
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

    # Save model responses for quality comparison
    responses_path = outpath.rsplit(".", 1)[0] + "_responses.md"
    _save_responses(responses_path, scenario, results, label, args.model, backend_key)
    print(f"  Responses: {responses_path}")

    # Track saved files so we can clean up on abort
    _saved_files.extend([outpath, md_path, responses_path])

    return warm_up_time


def _save_responses(path, scenario, results, label, model, backend):
    """Save model responses to a readable markdown file for quality comparison."""
    with open(path, "w") as f:
        f.write(f"# {scenario['name']} — {model} via {backend}\n\n")
        f.write(f"**Label:** {label}  \n")
        f.write(f"**Mode:** {scenario.get('mode', 'conversation')}  \n\n")
        f.write("---\n\n")

        for r in results:
            response = r.pop("_response", None)
            user = r.pop("_user", None)
            if response is None:
                continue
            turn = r.get("turn", "?")
            run = r.get("run", 1)
            tps = r.get("gen_tps", 0)
            total = r.get("total", 0)

            f.write(f"## Turn {turn} (run {run})\n\n")
            f.write(f"**User:** {user}\n\n")
            f.write(f"**Assistant** ({r.get('output_tokens', 0)} tokens, {tps} tok/s, {total:.1f}s total):\n\n")
            f.write(f"{response}\n\n")
            f.write("---\n\n")


# Files saved during the current run — cleaned up on Ctrl+C or errors
_saved_files = []


def _cleanup_saved_files():
    """Remove result files from an incomplete run."""
    for f in _saved_files:
        try:
            if os.path.exists(f):
                os.remove(f)
        except OSError:
            pass
    if _saved_files:
        print(f"\n  Cleaned up {len(_saved_files)} result files from incomplete run.")
        _saved_files.clear()


def main():
    parser = argparse.ArgumentParser(
        description="LLM inference benchmark — measures TTFT + generation speed per turn"
    )
    parser.add_argument("--scenario", default=None,
                        help="Run a single scenario JSON file. Default: runs ALL scenarios.")
    parser.add_argument("--backend", choices=["ollama", "lmstudio", "llama-server", "minimax", "openai"],
                        default="ollama", help="Inference backend (default: ollama)")
    parser.add_argument("--backend-label", default=None,
                        help="Custom backend name for result paths and metadata (e.g. omlx, vllm)")
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
    parser.add_argument("--no-think", action="store_true",
                        help="Disable thinking in the Qwen3.5 chat template before running. "
                             "Backs up the original template and restores it when done (or on error/Ctrl+C).")
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
            time.sleep(3)
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

    # ── Disable thinking if requested ─────────────────────────────────
    # Patches the Qwen3.5 chat template to inject a pre-closed <think>
    # block. The original is backed up and restored in ALL cases:
    # normal exit, errors, and Ctrl+C.
    thinking_backup = None
    template_path = None
    if args.no_think:
        template_path = find_chat_template(args.backend, args.model)
        if template_path:
            thinking_backup = disable_thinking(template_path)
        else:
            print(f"  Warning: --no-think ignored, no chat template found for {args.backend}/{args.model}",
                  file=sys.stderr)
    # ── Set up Ctrl+C / SIGTERM handler ─────────────────────────────
    # Clean up result files and restore thinking template on abort.
    def _abort_handler(signum, frame):
        print("\n\n  Benchmark interrupted.")
        _cleanup_saved_files()
        if thinking_backup and template_path:
            restore_thinking(template_path, thinking_backup)
        sys.exit(1)
    signal.signal(signal.SIGINT, _abort_handler)
    signal.signal(signal.SIGTERM, _abort_handler)

    try:
        if args.scenario:
            # Run a single scenario
            scenario_path = args.scenario if os.path.isabs(args.scenario) else os.path.join(script_dir, args.scenario)

            # Pre-flight: check context window is large enough
            scenario_data = load_scenario(scenario_path)
            max_ctx, max_out = estimate_max_context(scenario_data)
            check_context_size(stream_fn, base_url, args.model, args.backend, max_ctx + max_out)

            run_single(args, scenario_path, script_dir, stream_fn, base_url, warm_up_done=False)
        else:
            # Default: run all scenarios
            scenarios = find_all_scenarios(script_dir)
            if not scenarios:
                print("Error: No scenario files found in scenarios/", file=sys.stderr)
                sys.exit(1)

            # Pre-flight: check context window against the most demanding scenario
            max_needed = 0
            for sp in scenarios:
                s = load_scenario(sp)
                ctx, out = estimate_max_context(s)
                max_needed = max(max_needed, ctx + out)
            check_context_size(stream_fn, base_url, args.model, args.backend, max_needed)

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
            backend_key = args.backend_label or args.backend
            model_slug = make_model_slug(args.model)
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
            print(f"  git commit -m \"results: {chip_slug} {backend_key} {model_slug}\"")
            print(f"  git push -u origin {branch}")
            print(f"  gh pr create --title \"results: {chip_slug}\" \\")
            print(f"    --body \"Benchmark results from {chip_slug} using {backend_key}\"")
            print(f"\n  Your numbers will be added to the comparison table at")
            print(f"  https://famstack.dev/guides/mlx-vs-gguf-apple-silicon")
            print(f"\n{'='*70}\n")
    except SystemExit:
        # sys.exit() from error handlers — clean up partial results
        _cleanup_saved_files()
        raise
    except Exception:
        _cleanup_saved_files()
        raise
    finally:
        # ── Always restore the original template ──────────────────────
        if template_path:
            restore_thinking(template_path, thinking_backup)


if __name__ == "__main__":
    main()
