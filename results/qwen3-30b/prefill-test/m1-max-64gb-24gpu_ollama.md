# Apple M1 Max / 64GB / 24 GPU cores

**Model:** qwen3:30b (30.5B, Q4_K_M)  
**Backend:** ollama  
**Scenario:** prefill-test (single-shot)  

| Turn | Context | Prefill | Gen | Gen tok/s | Effective tok/s | Total | Output |
|-----:|--------:|--------:|----:|----------:|----------------:|------:|-------:|
| 1 | 655 | 1.59s | 3.49s | 43.0 | **29.5** | 5.08s | 150 |
| 2 | 1,453 | 3.56s | 4.00s | 37.5 | **19.9** | 7.56s | 150 |
| 3 | 3,015 | 9.68s | 5.04s | 29.8 | **10.2** | 14.72s | 150 |
| 4 | 8,496 | 87.48s | 10.27s | 14.6 | **1.5** | 97.76s | 150 |

**Total prefill:** 102.3s  
**Total generation:** 22.8s  
**Total time:** 125.1s  
**Avg generation tok/s:** 31.2  
**Avg effective tok/s:** 4.8  
