# Apple M1 Max / 64GB / 24 GPU cores

**Model:** mlx-community/meta-llama-3.1-8B-instruct  
**Backend:** lmstudio  
**Scenario:** doc-summary (single-shot)  

| Turn | Context | Prefill | Gen | Gen tok/s | Effective tok/s | Total | Output |
|-----:|--------:|--------:|----:|----------:|----------------:|------:|-------:|
| 1 | 425 | 1.46s | 1.10s | 59.8 | **25.8** | 2.56s | 66 |
| 2 | 612 | 1.23s | 0.95s | 59.1 | **25.7** | 2.18s | 56 |
| 3 | 535 | 1.37s | 1.04s | 62.3 | **27.0** | 2.41s | 65 |
| 4 | 524 | 1.23s | 1.02s | 61.5 | **28.0** | 2.25s | 63 |
| 5 | 1,518 | 3.86s | 1.21s | 55.3 | **13.2** | 5.07s | 67 |

**Total prefill:** 9.1s  
**Total generation:** 5.3s  
**Total time:** 14.5s  
**Avg generation tok/s:** 59.6  
**Avg effective tok/s:** 21.9  
