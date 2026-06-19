# Apple M4 Max / 128GB / 40 GPU cores

**Model:** gemma-4-31b-it-mlx  
**Backend:** lmstudio  
**Scenario:** doc-summary (single-shot)  

| Turn | Context | Prefill | Gen | Gen tok/s | Effective tok/s | Total | Output |
|-----:|--------:|--------:|----:|----------:|----------------:|------:|-------:|
| 1 | 425 | 3.58s | 6.65s | 14.3 | **9.3** | 10.23s | 95 |
| 2 | 612 | 2.88s | 4.53s | 14.3 | **8.8** | 7.41s | 65 |
| 3 | 535 | 3.25s | 4.24s | 14.6 | **8.3** | 7.50s | 62 |
| 4 | 524 | 3.15s | 5.70s | 14.2 | **9.1** | 8.86s | 81 |
| 5 | 1,518 | 8.23s | 5.74s | 14.1 | **5.8** | 13.98s | 81 |

**Total prefill:** 21.1s  
**Total generation:** 26.9s  
**Total time:** 48.0s  
**Avg generation tok/s:** 14.3  
**Avg effective tok/s:** 8.0  
