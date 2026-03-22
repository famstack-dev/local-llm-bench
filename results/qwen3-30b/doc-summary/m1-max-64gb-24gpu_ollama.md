# Apple M1 Max / 64GB / 24 GPU cores

**Model:** qwen3:30b (30.5B, Q4_K_M)  
**Backend:** ollama  
**Scenario:** doc-summary (single-shot)  

| Turn | Context | Prefill | Gen | Gen tok/s | Effective tok/s | Total | Output |
|-----:|--------:|--------:|----:|----------:|----------------:|------:|-------:|
| 1 | 425 | 1.22s | 3.40s | 44.2 | **32.5** | 4.61s | 150 |
| 2 | 612 | 0.84s | 3.38s | 44.4 | **35.6** | 4.22s | 150 |
| 3 | 535 | 0.94s | 3.43s | 43.7 | **34.3** | 4.37s | 150 |
| 4 | 524 | 0.89s | 3.41s | 44.0 | **34.9** | 4.30s | 150 |
| 5 | 1,518 | 3.03s | 3.92s | 38.2 | **21.6** | 6.96s | 150 |

**Total prefill:** 6.9s  
**Total generation:** 17.5s  
**Total time:** 24.5s  
**Avg generation tok/s:** 42.9  
**Avg effective tok/s:** 30.7  
