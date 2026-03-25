# Apple M1 Max / 64GB / 24 GPU cores

**Model:** qwen/qwen3.5-35b-a3b  
**Backend:** lmstudio  
**Scenario:** prefill-test (single-shot)  

| Turn | Context | Prefill | Gen | Gen tok/s | Effective tok/s | Total | Output |
|-----:|--------:|--------:|----:|----------:|----------------:|------:|-------:|
| 1 | 655 | 2.90s | 4.34s | 29.7 | **17.8** | 7.24s | 129 |
| 2 | 1,453 | 4.06s | 5.16s | 28.9 | **16.2** | 9.22s | 149 |
| 3 | 3,015 | 8.66s | 5.22s | 28.5 | **10.7** | 13.88s | 149 |
| 4 | 8,496 | 37.81s | 5.58s | 26.7 | **3.4** | 43.38s | 149 |

**Total prefill:** 53.4s  
**Total generation:** 20.3s  
**Total time:** 73.7s  
**Avg generation tok/s:** 28.4  
**Avg effective tok/s:** 7.8  
