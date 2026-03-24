# Apple M2 Pro / 32GB / 19 GPU cores

**Model:** qwen3.5-35b-a3b  
**Backend:** lmstudio  
**Scenario:** prefill-test (single-shot)  

| Turn | Context | Prefill | Gen | Gen tok/s | Effective tok/s | Total | Output |
|-----:|--------:|--------:|----:|----------:|----------------:|------:|-------:|
| 1 | 655 | 6.11s | 2.08s | 62.9 | **16.0** | 8.19s | 131 |
| 2 | 1,453 | 8.85s | 2.44s | 59.5 | **12.8** | 11.29s | 145 |
| 3 | 3,015 | 15.48s | 1.76s | 59.0 | **6.0** | 17.24s | 104 |
| 4 | 8,496 | 54.82s | 2.91s | 50.1 | **2.5** | 57.73s | 146 |

**Total prefill:** 85.3s  
**Total generation:** 9.2s  
**Total time:** 94.5s  
**Avg generation tok/s:** 57.9  
**Avg effective tok/s:** 5.6  
