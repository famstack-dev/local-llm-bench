"""
Result storage and display helpers.

RESULT FORMAT:
  All benchmark results are stored as JSON files with a standard envelope:

  {
      "meta": {
          "scenario": "agent",              # which scenario was run
          "label": "Ollama GGUF",           # human-readable run label
          "backend": "ollama",              # which backend adapter was used
          "model": "qwen3.5:35b-a3b",      # model identifier
          "base_url": "http://...",         # backend URL
          "runs": 1,                        # how many consecutive runs
          "max_tokens": 500,                # output token limit
          "timestamp": "2026-03-09T14:30",  # when the benchmark ran
          "hostname": "mac-merlin.local"    # which machine ran it
      },
      "results": [
          {
              "turn": 1,           # turn number within the conversation
              "run": 1,            # which run (for multi-run benchmarks)
              "ctx_tokens_est": 575,  # estimated total context tokens
              "new_tokens_est": 422,  # estimated NEW tokens this turn
              "ttft": 2.633,       # seconds waiting for first token
              "gen_time": 10.995,  # seconds of token generation
              "gen_tps": 18.8,     # generation tokens per second
              "total": 13.629,     # total wall clock time
              "output_tokens": 207 # tokens in the model's response
          },
          ...
      ]
  }

  The "meta" block is added automatically by save_results().
  The compare.py script reads these files and aligns results by turn number.
"""

import json
import os
import platform
import subprocess
import time


def _sysctl(key):
    """Read a single sysctl value. Returns None on failure."""
    try:
        return subprocess.check_output(
            ["sysctl", "-n", key], stderr=subprocess.DEVNULL,
        ).decode().strip()
    except (subprocess.SubprocessError, FileNotFoundError):
        return None


def _get_ollama_env(key):
    """Read an Ollama env var. Checks os.environ first, then launchctl.

    Users set these via 'launchctl setenv' which Ollama picks up on restart,
    but the bench.py process only inherits them if they were also exported
    in the shell. Checking launchctl covers both cases.
    """
    val = os.environ.get(key)
    if val:
        return val
    try:
        result = subprocess.check_output(
            ["launchctl", "getenv", key], stderr=subprocess.DEVNULL,
        ).decode().strip()
        return result if result else None
    except (subprocess.SubprocessError, FileNotFoundError):
        return None


def get_system_info():
    """
    Collect hardware and OS specs for the current machine.

    Designed for the community comparison use case — result files should be
    self-documenting and shareable without revealing personal information.

    WHAT WE COLLECT (and why):
      - chip: "Apple M1 Max" — the primary hardware identifier
      - gpu_cores: 24 — differentiates M1 Pro 14-core vs 16-core, etc.
                   This is the #1 factor for Metal inference performance.
      - cpu_cores: 10 — total CPU cores (affects prefill on some engines)
      - cpu_cores_performance: 8 — P-cores (fast cores)
      - cpu_cores_efficiency: 2 — E-cores (background cores)
      - memory_gb: 64 — unified memory size (determines max model size)
      - gpu_wired_limit_mb: 8192 — GPU wired memory limit (if changed from default)
      - os_version: "26.2" — macOS version
      - arch: "arm64" — architecture
      - ollama.flash_attention: "1" — if OLLAMA_FLASH_ATTENTION is set
      - ollama.kv_cache_type: "q4_0" — if OLLAMA_KV_CACHE_TYPE is set

    WHAT WE DON'T COLLECT:
      - hostname — identifies the user
      - base_url — useless for comparison, could leak custom URLs
      - username, IP, serial number — obvious privacy concerns

    On macOS, we use sysctl (instant) for most values and system_profiler
    (~300ms) for GPU core count which sysctl doesn't expose.
    """
    info = {
        "os": platform.system(),
        "os_version": platform.mac_ver()[0] or platform.release(),
        "arch": platform.machine(),
    }

    if platform.system() == "Darwin":
        # Chip name (e.g. "Apple M1 Max")
        chip = _sysctl("machdep.cpu.brand_string")
        if chip:
            info["chip"] = chip

        # Total memory in bytes → GB
        mem = _sysctl("hw.memsize")
        if mem:
            try:
                info["memory_gb"] = int(mem) // (1024 ** 3)
            except ValueError:
                pass

        # CPU core counts — total, P-cores (fast), E-cores (efficiency)
        ncpu = _sysctl("hw.ncpu")
        if ncpu:
            try:
                info["cpu_cores"] = int(ncpu)
            except ValueError:
                pass

        p_cores = _sysctl("hw.perflevel0.logicalcpu")
        if p_cores:
            try:
                info["cpu_cores_performance"] = int(p_cores)
            except ValueError:
                pass

        e_cores = _sysctl("hw.perflevel1.logicalcpu")
        if e_cores:
            try:
                info["cpu_cores_efficiency"] = int(e_cores)
            except ValueError:
                pass

        # GPU core count — the #1 differentiator for Metal inference.
        # sysctl doesn't expose this, so we use system_profiler (~300ms).
        try:
            sp_output = subprocess.check_output(
                ["system_profiler", "SPDisplaysDataType"],
                stderr=subprocess.DEVNULL,
            ).decode()
            for line in sp_output.splitlines():
                if "Total Number of Cores" in line:
                    gpu_cores = int(line.split(":")[-1].strip())
                    info["gpu_cores"] = gpu_cores
                    break
        except (subprocess.SubprocessError, FileNotFoundError, ValueError):
            pass

        # GPU wired memory limit — affects whether large models hit swap.
        # Default is typically ~75% of physical memory. Users can raise it
        # with: sudo sysctl iogpu.wired_limit_mb=8192
        wired_limit = _sysctl("iogpu.wired_limit_mb")
        if wired_limit:
            try:
                info["gpu_wired_limit_mb"] = int(wired_limit)
            except ValueError:
                pass

    # Ollama environment settings that affect inference performance.
    # These are set via: launchctl setenv OLLAMA_FLASH_ATTENTION 1
    ollama_settings = {}
    fa = _get_ollama_env("OLLAMA_FLASH_ATTENTION")
    if fa:
        ollama_settings["flash_attention"] = fa
    kv = _get_ollama_env("OLLAMA_KV_CACHE_TYPE")
    if kv:
        ollama_settings["kv_cache_type"] = kv
    if ollama_settings:
        info["ollama"] = ollama_settings

    return info


def make_chip_slug(system_info=None):
    """
    Generate a deterministic hardware slug from system info.

    Examples:
      "Apple M1 Max", 64GB, 24 GPU cores → "m1-max-64gb-24gpu"
      "Apple M4 Pro", 48GB, 20 GPU cores → "m4-pro-48gb-20gpu"

    Two machines with the same chip/memory/GPU get the same slug,
    which is intentional — their numbers should be comparable.
    """
    if system_info is None:
        system_info = get_system_info()

    chip = system_info.get("chip", "unknown")
    # "Apple M1 Max" → "m1-max"
    chip_short = chip.lower().replace("apple ", "").replace(" ", "-")
    mem = system_info.get("memory_gb", "")
    gpu = system_info.get("gpu_cores", "")

    parts = [chip_short]
    if mem:
        parts.append(f"{mem}gb")
    if gpu:
        parts.append(f"{gpu}gpu")
    return "-".join(parts)


def make_model_slug(model_name):
    """
    Normalize a model identifier into a filesystem-safe slug.

    Strips HuggingFace org prefixes and packaging suffixes so the same
    base model always lands in the same directory regardless of backend
    or packaging format.

    Examples:
      "qwen3.5:35b-a3b"                              → "qwen3.5-35b-a3b"
      "mlx-community/qwen3.5-35b-a3b"                → "qwen3.5-35b-a3b"
      "qwen/qwen3.5-35b-a3b"                         → "qwen3.5-35b-a3b"
      "lmstudio-community/Meta-Llama-3.1-8B-GGUF"    → "meta-llama-3.1-8b-instruct"
      "Qwen3.5-35B-A3B-4bit-fp16"                    → "qwen3.5-35b-a3b-4bit"
      "JANGQ-AI/Qwen3.5-35B-A3B-JANG_4K"             → "qwen3.5-35b-a3b-jang_4k"
    """
    slug = model_name

    # Strip HuggingFace org prefixes (mlx-community/, qwen/, meta-llama/, etc.)
    if "/" in slug:
        slug = slug.split("/", 1)[1]

    # Ollama uses colon as separator (qwen3.5:35b-a3b)
    slug = slug.replace(":", "-")

    slug = slug.lower()

    # Strip packaging suffixes — these are format details, not model identity.
    # Order matters: check longest suffixes first.
    for suffix in ("-gguf", "-mlx", "-fp16", "-bf16"):
        if slug.endswith(suffix):
            slug = slug[:-len(suffix)]
            break

    return slug


def make_config_suffix():
    """
    Generate a suffix for Ollama tuning flags, if any are set.

    Returns "" if no tuning flags are detected.
    Returns something like "fa-kvq4" if flash attention + q4_0 KV cache are on.
    """
    parts = []
    if _get_ollama_env("OLLAMA_FLASH_ATTENTION") == "1":
        parts.append("fa")
    kv = _get_ollama_env("OLLAMA_KV_CACHE_TYPE")
    if kv:
        parts.append(f"kv{kv.replace('_', '')}")
    return "-".join(parts)


def make_result_path(script_dir, model, scenario_name, backend, system_info=None):
    """
    Generate the output path for a benchmark result.

    Structure: results/<model>/<scenario>/<chip-slug>_<backend>[_<config>].json

    Examples:
      results/qwen3.5-35b-a3b/ops-agent/m1-max-64gb-24gpu_ollama.json
      results/qwen3.5-35b-a3b/ops-agent/m4-pro-48gb-20gpu_ollama_fa-kvq4.json
      results/qwen3.5-35b-a3b/doc-summary/m1-max-64gb-24gpu_lmstudio.json
    """
    model_slug = make_model_slug(model)
    chip_slug = make_chip_slug(system_info)
    config = make_config_suffix()

    filename = f"{chip_slug}_{backend}"
    if config:
        filename += f"_{config}"
    filename += ".json"

    return os.path.join(script_dir, "results", model_slug, scenario_name, filename)


def results_to_markdown(meta, results, system_info):
    """
    Generate a markdown summary of benchmark results.

    Saved alongside the JSON so results are readable on GitHub without
    any tooling. Contributors can also paste this into their PR description.
    """
    valid = [r for r in results if "error" not in r]
    if not valid:
        return ""

    # Header
    chip = system_info.get("chip", "Unknown")
    mem = system_info.get("memory_gb", "?")
    gpu = system_info.get("gpu_cores", "?")
    model_info = meta.get("model_info", {})
    model_name = model_info.get("name", "unknown")
    quant = model_info.get("quantization", "")
    param_size = model_info.get("parameter_size", "")
    backend = meta.get("backend", "unknown")
    scenario = meta.get("scenario", "unknown")
    mode = meta.get("mode", "conversation")
    ts = system_info.get("timestamp", meta.get("timestamp", ""))

    lines = []
    lines.append(f"# {chip} / {mem}GB / {gpu} GPU cores")
    lines.append("")

    model_desc = model_name
    if param_size:
        model_desc += f" ({param_size}"
        if quant:
            model_desc += f", {quant}"
        model_desc += ")"
    lines.append(f"**Model:** {model_desc}  ")
    lines.append(f"**Backend:** {backend}  ")
    lines.append(f"**Scenario:** {scenario} ({mode})  ")

    # Ollama tuning flags
    ollama_info = system_info.get("ollama", {})
    if ollama_info:
        flags = []
        if ollama_info.get("flash_attention"):
            flags.append("flash_attention=1")
        if ollama_info.get("kv_cache_type"):
            flags.append(f"kv_cache={ollama_info['kv_cache_type']}")
        if flags:
            lines.append(f"**Ollama config:** {', '.join(flags)}  ")

    wired = system_info.get("gpu_wired_limit_mb")
    if wired and wired > 0:
        lines.append(f"**GPU wired limit:** {wired} MB  ")

    lines.append("")

    # Turn-by-turn table
    lines.append("| Turn | Context | Prefill | Gen | Gen tok/s | Effective tok/s | Total | Output |")
    lines.append("|-----:|--------:|--------:|----:|----------:|----------------:|------:|-------:|")
    for r in valid:
        ctx = f"{r.get('ctx_tokens_est', 0):,}"
        effective = r['output_tokens'] / r['total'] if r['total'] > 0 else 0
        lines.append(
            f"| {r['turn']} | {ctx} | {r['ttft']:.2f}s | {r['gen_time']:.2f}s "
            f"| {r['gen_tps']:.1f} | **{effective:.1f}** | {r['total']:.2f}s | {r['output_tokens']} |"
        )

    # Summary
    total_ttft = sum(r["ttft"] for r in valid)
    total_gen = sum(r["gen_time"] for r in valid)
    total_time = sum(r["total"] for r in valid)
    total_output = sum(r["output_tokens"] for r in valid)
    avg_tps = sum(r["gen_tps"] for r in valid) / len(valid)
    avg_effective = total_output / total_time if total_time > 0 else 0

    lines.append("")
    lines.append(f"**Total prefill:** {total_ttft:.1f}s  ")
    lines.append(f"**Total generation:** {total_gen:.1f}s  ")
    lines.append(f"**Total time:** {total_time:.1f}s  ")
    lines.append(f"**Avg generation tok/s:** {avg_tps:.1f}  ")
    lines.append(f"**Avg effective tok/s:** {avg_effective:.1f}  ")

    return "\n".join(lines) + "\n"


def save_results(path, meta, results):
    """
    Save benchmark results as JSON + markdown.

    Saves two files:
      - <name>.json  — machine-readable, used by compare.py
      - <name>.md    — human-readable, visible on GitHub

    Automatically adds timestamp and system specs to the metadata so results
    are self-documenting and shareable. No personal information is included —
    no hostname, no IP, no username. See get_system_info() for what we collect.
    """
    system_info = get_system_info()
    envelope = {
        "meta": {
            **meta,
            "system": system_info,
            "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S"),
        },
        "results": results,
    }
    with open(path, "w") as f:
        json.dump(envelope, f, indent=2)

    # Save markdown alongside JSON
    md_path = path.rsplit(".", 1)[0] + ".md"
    md = results_to_markdown(meta, results, system_info)
    if md:
        with open(md_path, "w") as f:
            f.write(md)

    return path


def load_results(path):
    """
    Load benchmark results from a JSON file.

    Handles two formats:
    - Standard envelope: {"meta": {...}, "results": [...]}
    - Legacy bare array: [{turn: 1, ...}, ...]  (from early Part 1 scripts)

    Legacy arrays are wrapped in a minimal envelope so compare.py can
    handle them without special cases.
    """
    with open(path) as f:
        data = json.load(f)
    if isinstance(data, list):
        # Legacy format — wrap in envelope with the filename as label
        return {"meta": {"label": path}, "results": data}
    return data


def print_turn_header(backend=None):
    """
    Print the column header for the turn-by-turn benchmark table.

    The header adapts based on backend — Ollama gets an extra "PrEval" column
    showing how many prompt tokens were evaluated (from llama.cpp internals).
    """
    h = f"{'Turn':>4}  {'Ctx':>8}  {'New':>6}  {'Prefill':>9}  {'Gen':>7}  {'Tok/s':>6}  {'Eff t/s':>8}  {'Total':>7}  {'Out':>5}"
    if backend == "ollama":
        h += f"  {'PrEval':>7}"
    print(h)
    print("-" * len(h))


def print_turn_row(r, backend=None):
    """
    Print one row of the turn-by-turn benchmark table.

    Each row shows metrics for a single conversation turn:
    - Ctx: estimated total context tokens (all messages so far)
    - New: estimated NEW tokens added this turn (user msg + tool result)
    - TTFT: time to first token (prefill + network overhead)
    - Gen: generation time (first token to last token)
    - Tok/s: generation speed (output_tokens / gen_time)
    - Total: TTFT + Gen (what the user actually waits)
    - Out: how many tokens the model produced
    - PrEval: prompt tokens evaluated by llama.cpp (Ollama only)
    """
    effective = r['output_tokens'] / r['total'] if r['total'] > 0 else 0
    row = (
        f"{r['turn']:>4}  {r.get('ctx_tokens_est', 0):>8,}  {r.get('new_tokens_est', 0):>6,}  "
        f"{r['ttft']:>8.2f}s  {r['gen_time']:>6.2f}s  "
        f"{r['gen_tps']:>5.1f}  {effective:>7.1f}  {r['total']:>6.2f}s  "
        f"{r['output_tokens']:>5}"
    )
    if backend == "ollama":
        pe = r.get("prompt_eval_count")
        pe_str = str(pe) if pe is not None else "-"
        row += f"  {pe_str:>7}"
    print(row)


def print_summary(results, label=""):
    """
    Print aggregate stats for a benchmark run.

    Shows:
    - Total TTFT: cumulative time spent waiting for first tokens (staring at blank screen)
    - Total generation: cumulative time watching tokens stream
    - Total time: the full conversation wall clock
    - Avg gen tok/s: average generation speed across all turns
    """
    valid = [r for r in results if "error" not in r]
    if not valid:
        print("  No valid results.")
        return
    total_ttft = sum(r["ttft"] for r in valid)
    total_gen = sum(r["gen_time"] for r in valid)
    total_time = sum(r["total"] for r in valid)
    total_output = sum(r["output_tokens"] for r in valid)
    avg_tps = sum(r["gen_tps"] for r in valid) / len(valid)
    avg_effective = total_output / total_time if total_time > 0 else 0
    prefix = f"  {label} " if label else "  "
    print(f"{prefix}Total prefill:      {total_ttft:>7.1f}s")
    print(f"{prefix}Total generation:   {total_gen:>7.1f}s")
    print(f"{prefix}Total time:         {total_time:>7.1f}s")
    print(f"{prefix}Avg gen tok/s:      {avg_tps:>7.1f}")
    print(f"{prefix}Avg effective tok/s:{avg_effective:>7.1f}")
