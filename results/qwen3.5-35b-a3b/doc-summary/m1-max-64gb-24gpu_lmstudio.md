# Apple M1 Max / 64GB / 24 GPU cores

**Model:** qwen/qwen3.5-35b-a3b  
**Backend:** lmstudio  
**Scenario:** doc-summary (single-shot)  

| Turn | Context | Prefill | Gen | Gen tok/s | Effective tok/s | Total | Output |
|-----:|--------:|--------:|----:|----------:|----------------:|------:|-------:|
| 1 | 425 | 1.49s | 3.45s | 29.6 | **20.7** | 4.94s | 102 |
| 2 | 612 | 1.40s | 3.28s | 29.5 | **20.7** | 4.68s | 97 |
| 3 | 535 | 1.63s | 3.69s | 29.3 | **20.3** | 5.31s | 108 |
| 4 | 524 | 1.59s | 4.28s | 29.2 | **21.3** | 5.87s | 125 |
| 5 | 1,518 | 3.74s | 4.57s | 29.1 | **16.0** | 8.31s | 133 |

**Total prefill:** 9.9s  
**Total generation:** 19.3s  
**Total time:** 29.1s  
**Avg generation tok/s:** 29.3  
**Avg effective tok/s:** 19.4  
