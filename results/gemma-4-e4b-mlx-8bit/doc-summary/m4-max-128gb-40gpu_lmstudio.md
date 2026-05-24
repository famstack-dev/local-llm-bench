# Apple M4 Max / 128GB / 40 GPU cores

**Model:** gemma-4-e4b-it-mlx  
**Backend:** lmstudio  
**Scenario:** doc-summary (single-shot)  

| Turn | Context | Prefill | Gen | Gen tok/s | Effective tok/s | Total | Output |
|-----:|--------:|--------:|----:|----------:|----------------:|------:|-------:|
| 1 | 425 | 0.48s | 0.95s | 73.4 | **48.6** | 1.44s | 70 |
| 2 | 612 | 0.41s | 0.90s | 74.8 | **51.1** | 1.31s | 67 |
| 3 | 535 | 0.47s | 0.71s | 77.6 | **46.6** | 1.18s | 55 |
| 4 | 524 | 0.47s | 1.09s | 75.4 | **52.6** | 1.56s | 82 |
| 5 | 1,518 | 0.86s | 0.63s | 75.9 | **32.1** | 1.50s | 48 |

**Total prefill:** 2.7s  
**Total generation:** 4.3s  
**Total time:** 7.0s  
**Avg generation tok/s:** 75.4  
**Avg effective tok/s:** 46.1  
