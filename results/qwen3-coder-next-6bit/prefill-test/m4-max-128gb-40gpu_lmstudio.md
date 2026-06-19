# Apple M4 Max / 128GB / 40 GPU cores

**Model:** qwen/qwen3-coder-next  
**Backend:** lmstudio  
**Scenario:** prefill-test (single-shot)  

| Turn | Context | Prefill | Gen | Gen tok/s | Effective tok/s | Total | Output |
|-----:|--------:|--------:|----:|----------:|----------------:|------:|-------:|
| 1 | 655 | 1.58s | 2.05s | 72.3 | **40.8** | 3.62s | 148 |
| 2 | 1,453 | 1.51s | 2.11s | 68.3 | **39.8** | 3.62s | 144 |
| 3 | 3,015 | 3.12s | 2.14s | 69.5 | **28.3** | 5.26s | 149 |
| 4 | 8,496 | 13.55s | 2.30s | 62.1 | **9.0** | 15.85s | 143 |

**Total prefill:** 19.8s  
**Total generation:** 8.6s  
**Total time:** 28.4s  
**Avg generation tok/s:** 68.0  
**Avg effective tok/s:** 20.6  
