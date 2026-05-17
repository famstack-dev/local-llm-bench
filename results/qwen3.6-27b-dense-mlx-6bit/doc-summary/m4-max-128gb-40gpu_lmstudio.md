# Apple M4 Max / 128GB / 40 GPU cores

**Model:** qwen3.6-27b  
**Backend:** lmstudio  
**Scenario:** doc-summary (single-shot)  

| Turn | Context | Prefill | Gen | Gen tok/s | Effective tok/s | Total | Output |
|-----:|--------:|--------:|----:|----------:|----------------:|------:|-------:|
| 1 | 425 | 2.97s | 4.40s | 20.0 | **11.9** | 7.37s | 88 |
| 2 | 612 | 2.73s | 4.41s | 20.2 | **12.5** | 7.13s | 89 |
| 3 | 535 | 3.10s | 4.75s | 20.4 | **12.4** | 7.85s | 97 |
| 4 | 524 | 2.98s | 5.19s | 20.4 | **13.0** | 8.17s | 106 |
| 5 | 1,518 | 7.19s | 4.58s | 20.1 | **7.8** | 11.77s | 92 |

**Total prefill:** 19.0s  
**Total generation:** 23.3s  
**Total time:** 42.3s  
**Avg generation tok/s:** 20.2  
**Avg effective tok/s:** 11.2  
