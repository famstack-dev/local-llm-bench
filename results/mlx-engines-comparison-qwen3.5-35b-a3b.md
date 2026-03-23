Benchmark comparison of four MLX inference engines for running Qwen3.5-35B-A3B-4bit on Apple Silicon: oMLX, Rapid-MLX, mlx-openai-server, and LM Studio. Tests prefill speed, generation throughput, and effective tokens per second across four real-world scenarios on an M1 Max with 64GB RAM.

# Qwen3.5-35B-A3B-4bit: Backend Comparison (M1 Max 64GB, 24 GPU)

Tested: 2026-03-23

| Scenario | Backend | Prefill | Gen tok/s | Eff tok/s | Total |
|---|---|---:|---:|---:|---:|
| **creative-writing** | LM Studio | 13.4s | 58.8 | 38.3 | 38.5s |
| | mlx-openai-server | 1.9s | 62.6 | 57.8 | 25.2s |
| | Rapid-MLX | 1.8s | 62.2 | 56.5 | 19.2s |
| | **oMLX** | **1.1s** | **58.8** | **55.8** | **21.3s** |
| **doc-summary** | LM Studio | 31.3s | 56.9 | 13.4 | 41.0s |
| | mlx-openai-server | 11.4s | 59.8 | 26.2 | 20.3s |
| | Rapid-MLX | 10.6s | 60.7 | 28.7 | 20.1s |
| | **oMLX** | **8.1s** | **57.9** | **31.1** | **17.4s** |
| **ops-agent** | LM Studio | 96.9s | 56.5 | 17.0 | 138.6s |
| | mlx-openai-server | 60.4s | 59.1 | 26.2 | 108.6s |
| | **Rapid-MLX** | **29.6s** | **59.9** | **35.6** | **72.9s** |
| | oMLX | 24.5s | 55.6 | 38.0 | 78.1s |
| **prefill-test** | LM Studio | 80.5s | 53.9 | 5.9 | 90.4s |
| | mlx-openai-server | 54.0s | 57.1 | 8.7 | 63.7s |
| | Rapid-MLX | 54.7s | 57.3 | 8.5 | 64.4s |
| | **oMLX** | **22.2s** | **54.1** | **16.4** | **32.1s** |

## Key findings

- **oMLX** wins on prefill-heavy scenarios. Tiered KV cache makes prefill 2-4x faster than Rapid-MLX and 4-7x faster than LM Studio.
- **Rapid-MLX** wins on ops-agent (72.9s vs 78.1s) and creative-writing (19.2s vs 21.3s) thanks to higher generation speed (~60 tok/s vs ~56 tok/s), offsetting slower prefill.
- **mlx-openai-server** performs similarly to Rapid-MLX on prefill but slightly behind on total time.
- **LM Studio** is slowest across the board.
- Prefill gap widens with context size. At 8K tokens: oMLX 15.7s, Rapid-MLX 39.2s, mlx-openai-server 38.2s, LM Studio ~49s.
- Generation speed ranking: Rapid-MLX/mlx-openai-server (~60-62 tok/s) > LM Studio (~57 tok/s) > oMLX (~55 tok/s).

---

This benchmark was conducted as part of ongoing research at [famstack.dev](https://famstack.dev).
