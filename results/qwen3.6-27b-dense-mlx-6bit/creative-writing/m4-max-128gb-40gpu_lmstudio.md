# Apple M4 Max / 128GB / 40 GPU cores

**Model:** qwen3.6-27b  
**Backend:** lmstudio  
**Scenario:** creative-writing (single-shot)  

| Turn | Context | Prefill | Gen | Gen tok/s | Effective tok/s | Total | Output |
|-----:|--------:|--------:|----:|----------:|----------------:|------:|-------:|
| 1 | 57 | 1.08s | 25.14s | 20.7 | **19.8** | 26.22s | 520 |
| 2 | 60 | 0.82s | 33.51s | 20.6 | **20.1** | 34.33s | 690 |
| 3 | 58 | 0.82s | 19.89s | 20.7 | **19.8** | 20.71s | 411 |

**Total prefill:** 2.7s  
**Total generation:** 78.5s  
**Total time:** 81.3s  
**Avg generation tok/s:** 20.7  
**Avg effective tok/s:** 19.9  
