# Apple M4 Max / 128GB / 40 GPU cores

**Model:** gemma-4-26b-a4b-it-mlx@6bit  
**Backend:** lmstudio  
**Scenario:** doc-summary (single-shot)  

| Turn | Context | Prefill | Gen | Gen tok/s | Effective tok/s | Total | Output |
|-----:|--------:|--------:|----:|----------:|----------------:|------:|-------:|
| 1 | 425 | 0.70s | 1.03s | 86.2 | **51.3** | 1.74s | 89 |
| 2 | 612 | 0.55s | 0.73s | 86.4 | **49.4** | 1.28s | 63 |
| 3 | 535 | 0.60s | 0.83s | 86.8 | **50.2** | 1.43s | 72 |
| 4 | 524 | 0.58s | 1.12s | 84.7 | **55.8** | 1.70s | 95 |
| 5 | 1,518 | 1.30s | 0.80s | 85.2 | **32.4** | 2.10s | 68 |

**Total prefill:** 3.7s  
**Total generation:** 4.5s  
**Total time:** 8.2s  
**Avg generation tok/s:** 85.9  
**Avg effective tok/s:** 46.9  
