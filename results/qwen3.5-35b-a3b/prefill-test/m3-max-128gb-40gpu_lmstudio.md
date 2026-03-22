# Apple M3 Max / 128GB / 40 GPU cores

**Model:** qwen3.5-35b-a3b  
**Backend:** lmstudio  
**Scenario:** prefill-test (single-shot)  

| Turn | Context | Prefill | Gen | Gen tok/s | Effective tok/s | Total | Output |
|-----:|--------:|--------:|----:|----------:|----------------:|------:|-------:|
| 1 | 655 | 3.64s | 1.41s | 90.0 | **25.2** | 5.05s | 127 |
| 2 | 1,453 | 4.30s | 1.68s | 87.0 | **24.4** | 5.98s | 146 |
| 3 | 3,015 | 5.91s | 1.61s | 85.9 | **18.4** | 7.52s | 138 |
| 4 | 8,496 | 17.52s | 1.85s | 80.4 | **7.7** | 19.38s | 149 |

**Total prefill:** 31.4s  
**Total generation:** 6.5s  
**Total time:** 37.9s  
**Avg generation tok/s:** 85.8  
**Avg effective tok/s:** 14.8  
