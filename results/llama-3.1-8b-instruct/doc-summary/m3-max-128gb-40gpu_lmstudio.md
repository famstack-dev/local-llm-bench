# Apple M3 Max / 128GB / 40 GPU cores

**Model:** llama-3.1-8b-instruct  
**Backend:** lmstudio  
**Scenario:** doc-summary (single-shot)  

| Turn | Context | Prefill | Gen | Gen tok/s | Effective tok/s | Total | Output |
|-----:|--------:|--------:|----:|----------:|----------------:|------:|-------:|
| 1 | 425 | 0.69s | 0.96s | 73.8 | **43.1** | 1.65s | 71 |
| 2 | 612 | 0.62s | 0.71s | 78.8 | **42.2** | 1.33s | 56 |
| 3 | 535 | 0.68s | 0.88s | 78.2 | **44.1** | 1.56s | 69 |
| 4 | 524 | 0.62s | 1.06s | 76.2 | **48.0** | 1.69s | 81 |
| 5 | 1,518 | 1.98s | 1.04s | 73.0 | **25.2** | 3.02s | 76 |

**Total prefill:** 4.6s  
**Total generation:** 4.7s  
**Total time:** 9.2s  
**Avg generation tok/s:** 76.0  
**Avg effective tok/s:** 38.2  
