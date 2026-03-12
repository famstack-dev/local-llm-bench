# local-llm-bench: Scenario-Based LLM Benchmark for Apple Silicon

- Compare engines, models, and quantizations across scenarios
- Measure how context size impacts performance
- See what you actually wait for, not just the tok/s counter

Works on any Apple Silicon Mac (M1 through M5, MacBook Air to Mac Studio).

## The Problem

LLM interfaces report generation speed: *"53 tok/s"*. That sounds fast. But every response starts with a **prefill phase** where the model processes your entire conversation history before producing the first token. As your conversation grows, prefill grows too, and nobody shows you that number.

In an 8-turn agent conversation, the model with 53 tok/s loses to the model with 28 tok/s because its prefill is 2x slower. **Generation speed alone is misleading.**

**Read the full analysis: [MLX vs llama.cpp on Apple Silicon](https://famstack.dev/guides/mlx-vs-gguf-apple-silicon)**

## What It Measures

```
[User sends message]
     |
     |  Prefill (Time To First Token)
     |  ← Model processes entire conversation history
     |  ← Grows with every turn (this is the hidden cost)
     v
[First token appears]
     |
     |  Generation (tok/s)
     |  ← Model produces output tokens
     |  ← Stays roughly constant
     v
[Response complete]
```

**We measure both phases and report two speed metrics:**

- **Generation tok/s** — what your UI shows. Output tokens / generation time. Stays roughly constant regardless of context size.
- **Effective tok/s** — what you actually experience. Output tokens / total time (prefill + generation). Drops as context grows because prefill eats more of the wall clock.

```
effective tok/s = output_tokens / (prefill_time + generation_time)
```

At 8K tokens of context, a model reporting 57 tok/s generation speed can have an effective throughput of 3 tok/s. That gap is what this benchmark makes visible.

**Scenario types:**
- **Multi-turn conversations**: agent workflows, chat sessions, tool-calling chains. Context grows each turn, revealing prefill scaling behavior.
- **Single-shot tasks**: document conversion, classification, summarization. One large input, one output. Pure prefill-vs-generation comparison.

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

Results are saved automatically with a path based on your hardware, model, and backend:

```
results/qwen3.5-35b-a3b/ops-agent/m1-max-64gb-24gpu_ollama.json
```

No `--label` or `--output` needed. The tool detects your chip, memory, GPU core count, and any Ollama tuning flags and builds the path for you.

By default the benchmark warms up the model before starting, so Turn 1 measures actual prefill, not model loading. Use `--cold` to include loading time.

### Compare Results

```bash
# Compare across backends for one model
python3 compare.py results/qwen3.5-35b-a3b/ops-agent/*.json

# Compare across hardware
python3 compare.py results/qwen3.5-35b-a3b/ops-agent/m1-max*_ollama.json \
                   results/qwen3.5-35b-a3b/ops-agent/m4-pro*_ollama.json
```

Example output:

```
==========================================================================================
  OPS-AGENT BENCHMARK COMPARISON
==========================================================================================

                     LM Studio GGUF     LM Studio MLX
                     ───────────────── ─────────────────
  Turn 1  Prefill             2.60s             3.33s
               Gen             7.71s             5.54s
             Total            10.31s             8.87s

  Turn 8  Prefill            11.38s            19.40s    ← prefill dominates
               Gen            10.63s             5.50s
             Total            22.02s            24.91s
──────────────────── ───────────────── ─────────────────
    Total Prefill             54.4s            101.8s
         Total Gen             76.8s             42.3s
        Total Time            131.2s            144.0s
     Avg Gen tok/s             28.2              54.2

  Winner (fastest total): LM Studio GGUF (131.2s)
  LM Studio MLX: +12.9s slower (9%)
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
#    → results/llama3.1-8b/ops-agent/m4-pro-48gb-20gpu_ollama.json
#    → results/llama3.1-8b/doc-summary/m4-pro-48gb-20gpu_ollama.json
#    → results/llama3.1-8b/creative-writing/m4-pro-48gb-20gpu_ollama.json
#    → results/llama3.1-8b/prefill-test/m4-pro-48gb-20gpu_ollama.json

# 4. Commit and open a PR
git checkout -b results/m4-pro
git add results/
git commit -m "results: M4 Pro 48GB Ollama llama3.1-8b"
git push -u origin results/m4-pro
gh pr create --title "results: M4 Pro 48GB" --body "Ran ops-agent scenario with Ollama"
```

The filename is generated from your hardware specs, so there are no merge conflicts between contributors. Run it with different backends or models and each gets its own file.

**Bonus points:** Run with Ollama tuning flags and the tool auto-detects them:

```bash
sudo sysctl iogpu.wired_limit_mb=8192
launchctl setenv OLLAMA_FLASH_ATTENTION 1
launchctl setenv OLLAMA_KV_CACHE_TYPE "q4_0"

# Restart Ollama, then:
python3 bench.py --model qwen3.5:35b-a3b
# → results/qwen3.5-35b-a3b/ops-agent/m1-max-64gb-24gpu_ollama_fa-kvq40.json
```

Your results will be added to the hardware comparison table on [famstack.dev](https://famstack.dev/guides/mlx-vs-gguf-apple-silicon).

## What You Can Compare

This benchmark helps answer questions like:

- **MLX vs llama.cpp (GGUF)**: Which inference engine is faster for your workload? MLX has higher tok/s but slower prefill. The crossover depends on context length.
- **Ollama vs raw llama-server**: How much overhead does Ollama add? Is its KV cache worth it?
- **Different models**: How does a 7B model compare to a 35B MoE model on your hardware? Where does memory bandwidth become the bottleneck?
- **Different quantizations**: Q4_K_M vs Q8_0 vs FP16. What's the real-world tradeoff?
- **Your Mac vs others**: Share your result JSON files and compare across machines. Mac Mini M2 vs MacBook Pro M3 vs Mac Studio M4. How much does the hardware matter?

## Supported Backends

| Backend | Flag | Default URL | Engine |
|---|---|---|---|
| Ollama | `--backend ollama` | `http://localhost:11434` | llama.cpp (GGUF) with KV cache, model management |
| LM Studio | `--backend lmstudio` | `http://localhost:1234` | MLX or llama.cpp depending on model format |
| llama-server | `--backend llama-server` | `http://localhost:8090` | Raw llama.cpp (GGUF), no wrapper overhead |

Override any URL with `--base-url`.

## Scenarios

Scenarios are JSON files that define what to benchmark. Each scenario has a system prompt and a sequence of turns that the benchmark replays against the model.

### Included Scenarios

| Scenario | Turns | Mode | Description |
|---|---|---|---|
| [ops-agent.json](scenarios/ops-agent.json) | 8 | conversation | Server ops agent with tool calls. JSON payloads, log analysis, growing context |
| [doc-summary.json](scenarios/doc-summary.json) | 5 | single-shot | Document classification. Short output from long input |
| [prefill-test.json](scenarios/prefill-test.json) | 4 | single-shot | Prefill scaling. Same short reply at 655, 1.5K, 3K, and 8.5K context |
| [creative-writing.json](scenarios/creative-writing.json) | 3 | single-shot | Long-form creative output (poems, fables). Short prompt, up to 2000 tokens output. Where high gen tok/s shines |

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

For single-shot benchmarks, create a scenario with one turn and a large user message (e.g., a document to summarize or classify).

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

## Results

Numbers show **effective tok/s** (generation tok/s in parentheses). Effective = what you actually experience. Generation = what the UI reports. Higher is better. Blank cells need your data.

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

> **See your Mac in that table with empty cells?** Run `python3 bench.py --model llama3.1:8b` and [open a PR](#contribute-your-results). Takes just five minutes. No dependencies required.

### Settings variations

The default results above use Ollama with stock settings. These additional tables track how tuning flags affect performance on the same hardware.

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

All source files include detailed inline comments explaining what each section does and why. Designed to be readable by non-Python developers.

## Analysis & Findings

We used this benchmark to investigate MLX vs GGUF performance and Ollama's prompt caching on Apple Silicon. The full analysis with data and methodology is published at **[famstack.dev](https://famstack.dev)**.

Raw data and research notes are in [docs/](docs/).

## License

MIT
