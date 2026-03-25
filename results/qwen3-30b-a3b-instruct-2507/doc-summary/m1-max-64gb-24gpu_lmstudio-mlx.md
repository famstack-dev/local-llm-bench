# Apple M1 Max / 64GB / 24 GPU cores

**Model:** qwen3-30b-a3b-instruct-2507-mlx  
**Backend:** lmstudio-mlx  
**Scenario:** doc-summary (single-shot)  

| Turn | Context | Prefill | Gen | Gen tok/s | Effective tok/s | Total | Output |
|-----:|--------:|--------:|----:|----------:|----------------:|------:|-------:|
| 1 | 425 | 1.79s | 2.15s | 53.4 | **29.2** | 3.94s | 115 |
| 2 | 612 | 1.45s | 1.59s | 54.7 | **28.6** | 3.04s | 87 |
| 3 | 535 | 1.66s | 1.94s | 53.2 | **28.6** | 3.60s | 103 |
| 4 | 524 | 1.60s | 2.20s | 54.0 | **31.3** | 3.81s | 119 |
| 5 | 1,518 | 4.23s | 2.95s | 49.1 | **20.2** | 7.18s | 145 |

**Total prefill:** 10.7s  
**Total generation:** 10.8s  
**Total time:** 21.6s  
**Avg generation tok/s:** 52.9  
**Avg effective tok/s:** 26.4  
