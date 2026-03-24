# local-llm-bench - Benchmark your local LLM use case

Scenario-based LLM benchmark for Apple Silicon. Measures what you actually wait for, not just the generation tok/s counter.
It runs **real scenarios** (agent workflows, document classification, creative writing) and compares backends, engines, and hardware on the same workloads.
You can easily add your own single-shot or conversational scenarios to test your actual use case with different backends, models, etc.

Your LLM UI says *"57 tok/s"*. But every response starts with a **prefill phase** where the model processes your entire conversation history before the first token appears. As context grows, prefill dominates. A model reporting 57 tok/s can deliver as low as 3 tok/s in practice.

This benchmark measures **effective throughput**: output tokens divided by total wall-clock time. The speed you experience, not the speed on screen.

```
effective tok/s = output_tokens / (prefill_time + generation_time)
```

[Full analysis: MLX vs llama.cpp on Apple Silicon](https://famstack.dev/guides/mlx-vs-gguf-apple-silicon) | [Discord](https://discord.gg/tT54FNyf) | [Bluesky](https://bsky.app/profile/famstack.dev) | [Reddit](https://www.reddit.com/user/arthware/)

## Quick Start

Python 3.8+, no dependencies. Just a running inference backend with a model loaded.

```bash
# Ollama (default)
python3 bench.py --model llama3.1:8b

# LM Studio
python3 bench.py --backend lmstudio --model mlx-community/qwen3.5-35b-a3b --no-think

# oMLX or any OpenAI-compatible endpoint
OPENAI_API_KEY=key python3 bench.py --backend openai --backend-label omlx \
  --base-url http://localhost:8000 --model "Qwen3.5-35B-A3B-4bit" --no-think

# Compare results
python3 compare.py results/<model>/<scenario>/*.json
```

Results auto-save to `results/<model>/<scenario>/<chip>_<backend>.json`.

> **Before you run:** Set your context window to at least **16K tokens**. Add `--no-think` for Qwen3.5 models. **[Setup Guide -->](docs/setup-guide.md)**

## Results

Effective tok/s (**bold**) with generation tok/s in parentheses. Higher is better.

### Qwen3.5-35B-A3B (thinking disabled)

| Hardware | Backend | Format | ops-agent | doc-summary | prefill-test | creative-writing |
|---|---|---|---:|---:|---:|---:|
| M3 Max (128GB, 40 GPU) | oMLX | MLX 4-bit | **71.3** (90.8) | **61.4** (93.8) | **22.6** (87.9) | **90.1** (94.3) |
| M3 Max (128GB, 40 GPU) | LM Studio | MLX | **37.1** (83.5) | **22.5** (87.3) | **14.8** (85.8) | **59.0** (92.2) |
| M1 Max (64GB, 24 GPU) | oMLX | MLX 4-bit fp16 | **47.3** (65.2) | **33.1** (65.9) | **12.4** (62.5) | **63.4** (70.2) |
| M1 Max (64GB, 24 GPU) | oMLX | MLX 4-bit | **37.5** (53.3) | **29.4** (55.5) | **27.8** (52.0) | **53.7** (56.2) |
| M1 Max (64GB, 24 GPU) | Rapid-MLX | MLX 4-bit | **35.6** (59.9) | **28.7** (60.7) | **8.5** (57.3) | **56.5** (62.2) |
| M1 Max (64GB, 24 GPU) | mlx-openai-server | MLX 4-bit | **26.2** (59.3) | **26.2** (59.8) | **8.7** (57.5) | **57.8** (62.7) |
| M1 Max (64GB, 24 GPU) | LM Studio | MLX | **17.0** (56.6) | **13.4** (56.8) | **5.9** (54.4) | **38.3** (58.9) |
| M1 Max (64GB, 24 GPU) | LM Studio | GGUF | **17.6** (28.2) | **19.4** (29.3) | **7.8** (28.4) | **27.7** (28.6) |
| M2 Pro (32GB, 19 GPU) | LM Studio | MLX | **17.6** (58.4) | **14.3** (60.4) | **5.6** (57.9) | **42.9** (62.5) |

[oMLX](https://github.com/jundot/omlx) wins every scenario thanks to its tiered KV cache. On M3 Max, effective throughput reaches **71 tok/s** in ops-agent — nearly 2x the M1 Max result. Generation speed is identical across MLX engines (~55-93 tok/s depending on hardware), but prefill speed varies dramatically: at 8K context, LM Studio MLX takes 49s to prefill while oMLX takes 1.7s (with its persistent SSD cache from a prior run — cold prefill is higher).

### Llama 3.1 8B

| Hardware | Backend | Format | ops-agent | doc-summary | prefill-test | creative-writing |
|---|---|---|---:|---:|---:|---:|
| M3 Max (128GB, 40 GPU) | LM Studio | MLX | **57.6** (70.8) | **38.2** (76.0) | **14.4** (65.6) | **75.2** (78.5) |
| M3 Max (128GB, 40 GPU) | oMLX | MLX | **53.3** (69.4) | **35.1** (71.1) | **14.5** (63.2) | **73.6** (76.9) |
| M1 Max (64GB, 24 GPU) | LM Studio | MLX | **40.7** (55.0) | **21.9** (59.6) | **8.4** (51.8) | **58.9** (62.1) |
| M1 Max (64GB, 24 GPU) | LM Studio | GGUF | **30.6** (36.4) | **18.5** (40.7) | **7.1** (33.4) | **38.1** (39.1) |
| M1 Max (64GB, 24 GPU) | Ollama | GGUF | **27.1** (33.4) | **18.9** (37.8) | **5.8** (30.7) | **38.6** (39.6) |

MLX wins across the board. At 8B the model fits comfortably in memory, prefill stays fast, and the ~1.5x generation speed advantage dominates. On M3 Max, LM Studio MLX edges out oMLX thanks to lower TTFT overhead at this model size.

### GLM-4.7-Flash

| Hardware | Backend | Format | ops-agent | doc-summary | prefill-test | creative-writing |
|---|---|---|---:|---:|---:|---:|
| M2 Pro (32GB, 19 GPU) | oMLX | MLX 4-bit | **25.4** (36.7) | **15.3** (39.1) | **5.2** (34.3) | **40.9** (42.8) |
| M2 Pro (32GB, 19 GPU) | LM Studio | MLX | **24.3** (38.5) | **16.4** (41.3) | **5.1** (35.4) | **41.4** (43.8) |

### Help fill this table

> Run the benchmark on your hardware and [open a PR](#contribute-your-results). Five minutes, no dependencies.

| Hardware | Backend | Format | ops-agent | doc-summary | prefill-test | creative-writing |
|---|---|---|---:|---:|---:|---:|
| M1 Max (64GB, 24 GPU) | Ollama | GGUF | **27.1** (33.4) | **18.9** (37.8) | **5.8** (30.7) | **38.6** (39.6) |
| M2 Pro (32GB, 19 GPU) | LM Studio | MLX | **17.6** (58.4) | **14.3** (60.4) | **5.6** (57.9) | **42.9** (62.5) |
| M3 Max (128GB, 40 GPU) | oMLX | MLX 4-bit | **71.3** (90.8) | **61.4** (93.8) | **22.6** (87.9) | **90.1** (94.3) |
| M4 / Pro / Max | | | | | | |

## Scenarios

Four real-world scenarios. All run by default, or pick one with `--scenario`.

| Scenario | Mode | What it tests |
|---|---|---|
| [ops-agent](scenarios/ops-agent.json) | 8-turn conversation | Agent with tool calls. Context grows every turn. |
| [doc-summary](scenarios/doc-summary.json) | 5 single-shot turns | Document classification. Long input, short output. |
| [prefill-test](scenarios/prefill-test.json) | 4 single-shot turns | Prefill scaling: 655 to 8.5K context, same short reply. |
| [creative-writing](scenarios/creative-writing.json) | 3 single-shot turns | Short prompt, long output (up to 2K tokens). |

You can [create your own scenarios](docs/setup-guide.md) as JSON files.

## Supported Backends

| Backend | Flag | Default URL |
|---|---|---|
| [Ollama](https://ollama.com/) | `--backend ollama` | `localhost:11434` |
| [LM Studio](https://lmstudio.ai/) | `--backend lmstudio` | `localhost:1234` |
| [oMLX](https://github.com/jundot/omlx) | `--backend openai --backend-label omlx` | `localhost:8000` |
| [llama-server](https://github.com/ggml-org/llama.cpp) | `--backend llama-server` | `localhost:8090` |
| [MiniMax](https://platform.minimax.io/) | `--backend minimax` | `api.minimax.io` |
| Any OpenAI-compatible | `--backend openai` | `localhost:8080` |

Override with `--base-url`. Use `--backend-label` to customize the name in result paths.

## Contribute Your Results

One data point is an anecdote. A table full of hardware is useful.

```bash
# 1. Fork and clone
git clone https://github.com/<you>/local-llm-bench && cd local-llm-bench

# 2. Run (auto-detects your hardware)
python3 bench.py --model llama3.1:8b

# 3. Commit and PR
git checkout -b results/my-hardware
git add results/
git commit -m "results: my hardware"
git push -u origin HEAD
gh pr create --title "results: my hardware" --body "Benchmark results"
```

Filenames encode your hardware specs, so there are no merge conflicts between contributors.

## Tuning

The benchmark auto-detects Ollama flags and includes them in result filenames.

**Ollama:** `OLLAMA_FLASH_ATTENTION=1` (faster prefill) | `OLLAMA_KV_CACHE_TYPE=q4_0` (4x smaller KV cache) | `iogpu.wired_limit_mb=8192` (more GPU memory). Restart Ollama after changes.

**LM Studio MLX:** Default prefill chunk size is 512. [Raising to 4096 nearly doubles prefill speed.](https://github.com/thornad/lmstudio-mlx-patch)

**All backends:** See the **[Setup Guide](docs/setup-guide.md)** for context window configuration, Qwen3.5 thinking mode, and step-by-step verification.

## License

MIT
