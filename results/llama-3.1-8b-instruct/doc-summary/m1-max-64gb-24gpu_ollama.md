# Apple M1 Max / 64GB / 24 GPU cores

**Model:** llama3.1:8b (8.0B, Q4_K_M)  
**Backend:** ollama  
**Scenario:** doc-summary (single-shot)  

| Turn | Context | Prefill | Gen | Gen tok/s | Effective tok/s | Total | Output |
|-----:|--------:|--------:|----:|----------:|----------------:|------:|-------:|
| 1 | 425 | 1.36s | 1.71s | 38.6 | **21.5** | 3.07s | 66 |
| 2 | 612 | 1.20s | 1.67s | 38.4 | **22.3** | 2.87s | 64 |
| 3 | 535 | 1.38s | 1.78s | 38.3 | **21.6** | 3.15s | 68 |
| 4 | 524 | 1.19s | 1.59s | 38.4 | **21.9** | 2.78s | 61 |
| 5 | 1,518 | 4.08s | 2.54s | 35.5 | **13.6** | 6.62s | 90 |

**Total prefill:** 9.2s  
**Total generation:** 9.3s  
**Total time:** 18.5s  
**Avg generation tok/s:** 37.8  
**Avg effective tok/s:** 18.9  
