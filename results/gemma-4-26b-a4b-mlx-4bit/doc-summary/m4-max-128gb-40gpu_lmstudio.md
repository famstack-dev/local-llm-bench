# Apple M4 Max / 128GB / 40 GPU cores

**Model:** gemma-4-26b-a4b-it-mlx@4bit  
**Backend:** lmstudio  
**Scenario:** doc-summary (single-shot)  

| Turn | Context | Prefill | Gen | Gen tok/s | Effective tok/s | Total | Output |
|-----:|--------:|--------:|----:|----------:|----------------:|------:|-------:|
| 1 | 425 | 0.69s | 0.94s | 107.9 | **62.3** | 1.62s | 101 |
| 2 | 612 | 0.51s | 0.54s | 108.5 | **55.6** | 1.04s | 58 |
| 3 | 535 | 0.56s | 0.62s | 109.4 | **57.7** | 1.18s | 68 |
| 4 | 524 | 0.55s | 0.91s | 106.7 | **66.7** | 1.45s | 97 |
| 5 | 1,518 | 1.23s | 0.82s | 105.3 | **42.0** | 2.05s | 86 |

**Total prefill:** 3.5s  
**Total generation:** 3.8s  
**Total time:** 7.3s  
**Avg generation tok/s:** 107.6  
**Avg effective tok/s:** 55.8  
