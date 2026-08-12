# Apple M2 Max / 64GB / 38 GPU cores

**Model:** Qwen3.6-35B-A3B-UD-MLX-fp16  
**Backend:** omlx  
**Scenario:** doc-summary (single-shot)  
**GPU wired limit:** 59392 MB  

| Turn | Context | Prefill | Gen | Gen tok/s | Effective tok/s | Total | Output |
|-----:|--------:|--------:|----:|----------:|----------------:|------:|-------:|
| 1 | 425 | 2.66s | 0.00s | 6335.8 | **0.4** | 2.66s | 1 |
| 2 | 612 | 2.56s | 0.00s | 6853.4 | **0.4** | 2.56s | 1 |
| 3 | 535 | 2.81s | 0.00s | 7145.3 | **0.4** | 2.81s | 1 |
| 4 | 524 | 2.63s | 0.00s | 6955.7 | **0.4** | 2.63s | 1 |
| 5 | 1,518 | 3.35s | 0.00s | 6132.0 | **0.3** | 3.35s | 1 |

**Total prefill:** 14.0s  
**Total generation:** 0.0s  
**Total time:** 14.0s  
**Avg generation tok/s:** 6684.4  
**Avg effective tok/s:** 0.4  
