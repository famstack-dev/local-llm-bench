# Apple M4 Max / 128GB / 40 GPU cores

**Model:** qwen3.6-35b-a3b  
**Backend:** lmstudio-mlx  
**Scenario:** doc-summary (single-shot)  

| Turn | Context | Prefill | Gen | Gen tok/s | Effective tok/s | Total | Output |
|-----:|--------:|--------:|----:|----------:|----------------:|------:|-------:|
| 1 | 425 | 0.61s | 1.24s | 90.4 | **60.7** | 1.84s | 112 |
| 2 | 612 | 0.54s | 0.95s | 90.8 | **58.0** | 1.48s | 86 |
| 3 | 535 | 0.58s | 0.97s | 93.7 | **58.5** | 1.55s | 91 |
| 4 | 524 | 0.58s | 1.03s | 92.9 | **59.7** | 1.61s | 96 |
| 5 | 1,518 | 1.10s | 1.13s | 90.9 | **46.1** | 2.24s | 103 |

**Total prefill:** 3.4s  
**Total generation:** 5.3s  
**Total time:** 8.7s  
**Avg generation tok/s:** 91.7  
**Avg effective tok/s:** 55.9  
