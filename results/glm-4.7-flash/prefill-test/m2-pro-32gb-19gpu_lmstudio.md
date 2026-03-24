# Apple M2 Pro / 32GB / 19 GPU cores

**Model:** glm-4.7-flash  
**Backend:** lmstudio  
**Scenario:** prefill-test (single-shot)  

| Turn | Context | Prefill | Gen | Gen tok/s | Effective tok/s | Total | Output |
|-----:|--------:|--------:|----:|----------:|----------------:|------:|-------:|
| 1 | 655 | 2.90s | 2.51s | 42.2 | **19.6** | 5.41s | 106 |
| 2 | 1,453 | 5.71s | 3.71s | 39.4 | **15.5** | 9.42s | 146 |
| 3 | 3,015 | 13.72s | 4.12s | 35.7 | **8.2** | 17.83s | 147 |
| 4 | 8,496 | 68.95s | 6.10s | 24.1 | **2.0** | 75.05s | 147 |

**Total prefill:** 91.3s  
**Total generation:** 16.4s  
**Total time:** 107.7s  
**Avg generation tok/s:** 35.4  
**Avg effective tok/s:** 5.1  
