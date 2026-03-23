# Apple M1 Max / 64GB / 24 GPU cores

**Model:** mlx-community/Qwen3.5-35B-A3B-4bit  
**Backend:** rapid-mlx  
**Scenario:** doc-summary (single-shot)  

| Turn | Context | Prefill | Gen | Gen tok/s | Effective tok/s | Total | Output |
|-----:|--------:|--------:|----:|----------:|----------------:|------:|-------:|
| 1 | 425 | 1.73s | 2.10s | 60.8 | **33.4** | 3.83s | 128 |
| 2 | 612 | 1.93s | 1.74s | 60.9 | **28.9** | 3.67s | 106 |
| 3 | 535 | 1.67s | 1.50s | 60.6 | **28.7** | 3.17s | 91 |
| 4 | 524 | 1.55s | 1.75s | 60.7 | **32.1** | 3.30s | 106 |
| 5 | 1,518 | 3.73s | 2.39s | 60.6 | **23.7** | 6.12s | 145 |

**Total prefill:** 10.6s  
**Total generation:** 9.5s  
**Total time:** 20.1s  
**Avg generation tok/s:** 60.7  
**Avg effective tok/s:** 28.7  
