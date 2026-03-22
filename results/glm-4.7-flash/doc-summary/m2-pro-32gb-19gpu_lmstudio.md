# Apple M2 Pro / 32GB / 19 GPU cores

**Model:** glm-4.7-flash  
**Backend:** lmstudio  
**Scenario:** doc-summary (single-shot)  

| Turn | Context | Prefill | Gen | Gen tok/s | Effective tok/s | Total | Output |
|-----:|--------:|--------:|----:|----------:|----------------:|------:|-------:|
| 1 | 425 | 2.00s | 0.79s | 43.3 | **12.2** | 2.79s | 34 |
| 2 | 612 | 1.78s | 0.55s | 42.2 | **9.9** | 2.33s | 23 |
| 3 | 535 | 2.01s | 2.10s | 40.5 | **20.7** | 4.10s | 85 |
| 4 | 524 | 1.90s | 3.54s | 41.3 | **26.9** | 5.43s | 146 |
| 5 | 1,518 | 5.19s | 1.61s | 39.1 | **9.3** | 6.80s | 63 |

**Total prefill:** 12.9s  
**Total generation:** 8.6s  
**Total time:** 21.4s  
**Avg generation tok/s:** 41.3  
**Avg effective tok/s:** 16.4  
