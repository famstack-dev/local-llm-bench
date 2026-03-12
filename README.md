# local-llm-bench

Scenario-based LLM benchmark for Apple Silicon. Measures what you actually wait for, not just the generation tok/s counter. Built for the [MLX vs llama.cpp analysis on famstack.dev](https://famstack.dev/guides/mlx-vs-gguf-apple-silicon).

## Results

Numbers show **effective tok/s** (generation tok/s in parentheses). Higher is better. Blank cells need your data.

**Effective tok/s** = output tokens / total time (prefill + generation). This is the speed you experience. Generation tok/s is the speed your UI reports. They diverge fast as context grows.

```
effective tok/s = output_tokens / (prefill_time + generation_time)
```

At 8K context, a model reporting 57 tok/s generation speed delivers 3 tok/s effective throughput. That gap is what this benchmark makes visible.

<!-- To regenerate: python3 results-table.py -->

### llama3.1:8b (Q4_K_M) via Ollama

| Hardware | ops-agent | doc-summary | prefill-test | creative-writing |
|---|---:|---:|---:|---:|
| M1 Max (64GB, 24 GPU) | **25.9** (32.5) | **17.3** (36.9) | **5.6** (29.4) | |
| M1 Pro (32GB, 16 GPU) | | | | |
| M2 Pro (32GB, 19 GPU) | | | | |
| M2 Max (64GB, 38 GPU) | | | | |
| M3 (16GB, 10 GPU) | | | | |
| M3 Pro (36GB, 18 GPU) | | | | |
| M3 Max (48GB, 40 GPU) | | | | |
| M4 (16GB, 10 GPU) | | | | |
| M4 Pro (24GB, 20 GPU) | | | | |
| M4 Pro (48GB, 20 GPU) | | | | |
| M4 Max (64GB, 40 GPU) | | | | |

> **See your Mac in that table with empty cells?** Run `python3 bench.py --model llama3.1:8b` and [open a PR](#contribute-your-results). Takes five minutes. No dependencies required.

### Settings variations

Default results above use Ollama with stock settings. These tables track how tuning flags affect performance on the same hardware.

#### Flash attention + quantized KV cache

```bash
sudo sysctl iogpu.wired_limit_mb=8192
launchctl setenv OLLAMA_FLASH_ATTENTION 1
launchctl setenv OLLAMA_KV_CACHE_TYPE "q4_0"
# Restart Ollama after setting env vars
```

| Hardware | Settings | ops-agent | doc-summary | prefill-test | creative-writing |
|---|---|---:|---:|---:|---:|
| M1 Max (64GB, 24 GPU) | fa + kv q4_0 | | | | |
| M4 Pro (48GB, 20 GPU) | fa + kv q4_0 | | | | |

#### Flash attention only

```bash
launchctl setenv OLLAMA_FLASH_ATTENTION 1
```

| Hardware | Settings | ops-agent | doc-summary | prefill-test | creative-writing |
|---|---|---:|---:|---:|---:|
| M1 Max (64GB, 24 GPU) | fa | | | | |

<!-- Add more settings tables here as we test them. The benchmark auto-detects
     OLLAMA_FLASH_ATTENTION and OLLAMA_KV_CACHE_TYPE and appends them to the
     result filename (e.g. m1-max-64gb-24gpu_ollama_fa-kvq40.json), so results
     from different configs never overwrite each other. -->

## What You Can Compare

- **MLX vs llama.cpp (GGUF)**: Which inference engine is faster for your workload? MLX has higher generation tok/s but slower prefill. The crossover depends on context length.
- **Ollama vs raw llama-server**: How much overhead does Ollama add? Is its KV cache worth it?
- **Models**: How does a 7B compare to a 35B MoE on your hardware? Where does memory bandwidth become the bottleneck?
- **Quantizations**: Q4_K_M vs Q8_0 vs FP16. Real-world tradeoff, not synthetic.
- **Your Mac vs others**: M2 MacBook Air vs M3 Pro MacBook Pro vs M4 Max Mac Studio. How much does the hardware matter?

## How It Works

LLM interfaces report generation speed: *"53 tok/s"*. Sounds fast. But every response starts with a **prefill phase** where the model processes your entire conversation history before producing the first token. As context grows, prefill grows. Nobody shows you that number.

In an 8-turn agent conversation, the model with 53 tok/s generation speed loses to the model with 28 tok/s because its prefill takes 2x longer.

```
[User sends message]
     |
     |  Prefill (Time To First Token)
     |  <- Model processes entire conversation history
     |  <- Grows with every turn (the hidden cost)
     v
[First token appears]
     |
     |  Generation (tok/s)
     |  <- Model produces output tokens
     |  <- Stays roughly constant
     v
[Response complete]
```

**Scenario types:**
- **Multi-turn conversations**: agent workflows, tool-calling chains. Context grows each turn, revealing prefill scaling behavior.
- **Single-shot tasks**: document conversion, classification. One large input, one output. Pure prefill-vs-generation comparison.

**Full analysis: [MLX vs llama.cpp on Apple Silicon](https://famstack.dev/guides/mlx-vs-gguf-apple-silicon)**

## Quick Start

### Requirements

- Python 3.8+ (stdlib only, no pip install needed)
- A running inference backend: [Ollama](https://ollama.com/), [LM Studio](https://lmstudio.ai/), or raw [llama-server](https://github.com/ggml-org/llama.cpp)
- A model loaded in that backend

### Run a Benchmark

```bash
# Run all scenarios (default)
python3 bench.py --model llama3.1:8b

# Run a single scenario
python3 bench.py --model llama3.1:8b --scenario scenarios/creative-writing.json

# Against LM Studio (MLX model)
python3 bench.py --backend lmstudio --model mlx-community/qwen3.5-35b-a3b

# Against raw llama-server (llama.cpp without Ollama)
python3 bench.py --backend llama-server --base-url http://localhost:8090 --model qwen3.5:35b-a3b

# Include model loading time in the measurement
python3 bench.py --model llama3.1:8b --cold
```

Results are saved automatically based on your hardware, model, and backend:

```
results/qwen3.5-35b-a3b/ops-agent/m1-max-64gb-24gpu_ollama.json
```

No `--label` or `--output` needed. The tool detects your chip, memory, GPU core count, and any Ollama tuning flags.

By default the benchmark warms up the model before starting, so Turn 1 measures actual prefill, not model loading. Use `--cold` to include loading time.

### Compare Results

```bash
# Compare across backends for one model
python3 compare.py results/qwen3.5-35b-a3b/ops-agent/*.json

# Compare across hardware
python3 compare.py results/qwen3.5-35b-a3b/ops-agent/m1-max*_ollama.json \
                   results/qwen3.5-35b-a3b/ops-agent/m4-pro*_ollama.json
```

## Contribute Your Results

We have one data point: an M1 Max. One data point is an anecdote. A table full of hardware is useful.

**If you have any Apple Silicon Mac, we want your numbers.** M2 MacBook Air, M3 Pro MacBook Pro, M4 Mac Mini, M4 Max MacBook Pro. The benchmark takes five minutes and needs zero dependencies.

### How to contribute

```bash
# 1. Fork and clone
git clone https://github.com/<your-username>/local-llm-bench
cd local-llm-bench

# 2. Run all scenarios (picks up your hardware automatically)
python3 bench.py --model llama3.1:8b

# 3. Results land in the right place
#    results/llama3.1-8b/ops-agent/m4-pro-48gb-20gpu_ollama.json
#    results/llama3.1-8b/doc-summary/m4-pro-48gb-20gpu_ollama.json
#    results/llama3.1-8b/creative-writing/m4-pro-48gb-20gpu_ollama.json
#    results/llama3.1-8b/prefill-test/m4-pro-48gb-20gpu_ollama.json

# 4. Commit and open a PR
git checkout -b results/m4-pro
git add results/
git commit -m "results: M4 Pro 48GB Ollama llama3.1-8b"
git push -u origin results/m4-pro
gh pr create --title "results: M4 Pro 48GB" --body "Ran all scenarios with Ollama"
```

The filename is generated from your hardware specs, so there are no merge conflicts between contributors.

**Bonus points:** Run with Ollama tuning flags and the tool auto-detects them:

```bash
sudo sysctl iogpu.wired_limit_mb=8192
launchctl setenv OLLAMA_FLASH_ATTENTION 1
launchctl setenv OLLAMA_KV_CACHE_TYPE "q4_0"

# Restart Ollama, then:
python3 bench.py --model qwen3.5:35b-a3b
# results/qwen3.5-35b-a3b/ops-agent/m1-max-64gb-24gpu_ollama_fa-kvq40.json
```

## Tuning Flags

These settings can significantly change benchmark results. The benchmark auto-detects Ollama flags and includes them in the result metadata and filename.

### Ollama

| Flag | Default | How to set | What it does |
|---|---|---|---|
| `OLLAMA_FLASH_ATTENTION` | off | `launchctl setenv OLLAMA_FLASH_ATTENTION 1` | Enables flash attention in llama.cpp. Reduces memory usage during attention and speeds up prefill, especially at longer context. |
| `OLLAMA_KV_CACHE_TYPE` | `f16` | `launchctl setenv OLLAMA_KV_CACHE_TYPE "q4_0"` | Quantizes the KV cache from fp16 to 4-bit. Cuts KV cache memory by ~4x, allowing longer conversations before performance drops. Slight quality trade-off at very high context. Options: `q8_0`, `q4_0`. |
| `iogpu.wired_limit_mb` | auto | `sudo sysctl iogpu.wired_limit_mb=8192` | Raises the macOS GPU wired memory limit. Prevents large models from hitting swap by allowing more unified memory to be pinned for GPU use. Resets on reboot. |

Restart Ollama after setting env vars (`brew services restart ollama` or `launchctl kickstart -k gui/$(id -u)/com.ollama.ollama`).

### LM Studio (MLX engine)

| Flag | Default | Where to change | What it does |
|---|---|---|---|
| Prefill chunk size | 512 | LM Studio settings or [manual patch](https://github.com/thornad/lmstudio-mlx-patch) | Controls how many tokens MLX processes per batch during prefill. The default 512 is conservative. Raising to 4096 can nearly double prefill speed. Diminishing returns above 4096. |

Prefill chunk size benchmarks from [thornad/lmstudio-mlx-patch](https://github.com/thornad/lmstudio-mlx-patch):

| Chunk size | Prefill speed | vs default |
|---:|---:|---|
| 512 (default) | 65 tok/s | baseline |
| 1024 | 102 tok/s | +57% |
| 2048 | 119 tok/s | +83% |
| **4096** | **129 tok/s** | **+98%** |
| 8192 | 128 tok/s | +97% (higher variance) |

## Supported Backends

| Backend | Flag | Default URL | Engine |
|---|---|---|---|
| Ollama | `--backend ollama` | `http://localhost:11434` | llama.cpp (GGUF) with KV cache, model management |
| LM Studio | `--backend lmstudio` | `http://localhost:1234` | MLX or llama.cpp depending on model format |
| llama-server | `--backend llama-server` | `http://localhost:8090` | Raw llama.cpp (GGUF), no wrapper overhead |

Override any URL with `--base-url`.

## Scenarios

Scenarios are JSON files that define what to benchmark. Each scenario has a system prompt and a sequence of turns replayed against the model.

### Included Scenarios

| Scenario | Turns | Mode | Description |
|---|---|---|---|
| [ops-agent.json](scenarios/ops-agent.json) | 8 | conversation | Server ops agent with tool calls. JSON payloads, log analysis, growing context |
| [doc-summary.json](scenarios/doc-summary.json) | 5 | single-shot | Document classification. Short output from long input |
| [prefill-test.json](scenarios/prefill-test.json) | 4 | single-shot | Prefill scaling. Same short reply at 655, 1.5K, 3K, and 8.5K context |
| [creative-writing.json](scenarios/creative-writing.json) | 3 | single-shot | Long-form creative output (poems, fables). Short prompt, up to 2000 tokens output |

### Creating Your Own

```json
{
  "name": "my-scenario",
  "description": "What this scenario tests",
  "system_prompt": "You are a helpful assistant.",
  "max_tokens": 500,
  "temperature": 0.6,
  "turns": [
    {
      "user": "Hello, how are you?"
    },
    {
      "user": "Can you check something for me?",
      "tool": "my_tool",
      "tool_result": "{ \"status\": \"ok\" }"
    }
  ]
}
```

Each turn has a `user` message. Optionally, `tool` and `tool_result` simulate the assistant calling a tool. This adds realistic context growth, just like agent frameworks do.

## Result Format

Results are saved as JSON with a metadata envelope. The path encodes your hardware, model, and configuration:

```
results/<model>/<scenario>/<chip-slug>_<backend>[_<config>].json
```

Examples:
```
results/qwen3.5-35b-a3b/ops-agent/m1-max-64gb-24gpu_ollama.json
results/qwen3.5-35b-a3b/ops-agent/m4-pro-48gb-20gpu_lmstudio.json
results/qwen3.5-35b-a3b/ops-agent/m1-max-64gb-24gpu_ollama_fa-kvq40.json
```

Each file contains:

```json
{
  "meta": {
    "scenario": "ops-agent",
    "label": "m1-max-64gb-24gpu ollama",
    "backend": "ollama",
    "model_info": {
      "name": "qwen3.5:35b-a3b",
      "family": "qwen3",
      "parameter_size": "35.1B",
      "quantization": "Q4_K_M"
    },
    "system": {
      "chip": "Apple M1 Max",
      "memory_gb": 64,
      "gpu_cores": 24,
      "cpu_cores": 10,
      "gpu_wired_limit_mb": 0,
      "ollama": {
        "flash_attention": "1",
        "kv_cache_type": "q4_0"
      }
    },
    "timestamp": "2026-03-09T14:30:00"
  },
  "results": [
    {
      "turn": 1,
      "ctx_tokens_est": 575,
      "ttft": 2.633,
      "gen_time": 10.995,
      "gen_tps": 18.8,
      "total": 13.629,
      "output_tokens": 207
    }
  ]
}
```

## Project Structure

```
local-llm-bench/
├── bench.py              # Main benchmark runner
├── compare.py            # Side-by-side comparison tool
├── results-table.py      # Regenerate the results overview table
├── lib/
│   ├── backends.py       # Backend adapters (Ollama, LM Studio, llama-server)
│   └── output.py         # Result storage, slug generation, display helpers
├── scenarios/
│   ├── ops-agent.json    # 8-turn server ops conversation with tool calls
│   ├── doc-summary.json  # 5-turn document classification
│   ├── prefill-test.json # Prefill scaling at different context sizes
│   └── creative-writing.json  # Long-form creative output (poems, fables)
├── results/              # Saved benchmark results
│   └── <model>/
│       └── <scenario>/
│           └── <chip>_<backend>[_<config>].json
└── docs/
    ├── paper.md          # Full MLX vs GGUF analysis
    ├── part2-design.md   # Part 2 design (caching hypotheses)
    └── part2-findings.md # Part 2 results
```

## License

MIT
