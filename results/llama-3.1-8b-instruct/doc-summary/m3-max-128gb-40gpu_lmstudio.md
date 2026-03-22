# Apple M3 Max / 128GB / 40 GPU cores

**Model:** llama-3.1-8b-instruct  
**Backend:** lmstudio  
**Scenario:** doc-summary (single-shot)  

| Turn | Context | Prefill | Gen | Gen tok/s | Effective tok/s | Total | Output |
|-----:|--------:|--------:|----:|----------:|----------------:|------:|-------:|
| 1 | 425 | 0.90s | 3.20s | 23.2 | **18.1** | 4.09s | 74 |
| 2 | 612 | 0.78s | 2.86s | 24.1 | **18.9** | 3.64s | 69 |
| 3 | 535 | 0.84s | 2.78s | 24.1 | **18.5** | 3.62s | 67 |
| 4 | 524 | 0.83s | 2.78s | 24.5 | **18.9** | 3.60s | 68 |
| 5 | 1,518 | 1.90s | 3.04s | 22.4 | **13.8** | 4.94s | 68 |

**Total prefill:** 5.2s  
**Total generation:** 14.7s  
**Total time:** 19.9s  
**Avg generation tok/s:** 23.7  
**Avg effective tok/s:** 17.4  
