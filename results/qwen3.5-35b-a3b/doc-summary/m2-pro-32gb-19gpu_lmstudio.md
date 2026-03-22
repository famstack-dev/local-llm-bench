# Apple M2 Pro / 32GB / 19 GPU cores

**Model:** qwen3.5-35b-a3b  
**Backend:** lmstudio  
**Scenario:** doc-summary (single-shot)  

| Turn | Context | Prefill | Gen | Gen tok/s | Effective tok/s | Total | Output |
|-----:|--------:|--------:|----:|----------:|----------------:|------:|-------:|
| 1 | 425 | 5.15s | 2.06s | 60.7 | **17.3** | 7.21s | 125 |
| 2 | 612 | 5.11s | 1.50s | 59.8 | **13.6** | 6.61s | 90 |
| 3 | 535 | 5.49s | 1.98s | 60.7 | **16.1** | 7.47s | 120 |
| 4 | 524 | 5.31s | 1.54s | 61.1 | **13.7** | 6.85s | 94 |
| 5 | 1,518 | 8.50s | 2.07s | 59.5 | **11.6** | 10.57s | 123 |

**Total prefill:** 29.6s  
**Total generation:** 9.1s  
**Total time:** 38.7s  
**Avg generation tok/s:** 60.4  
**Avg effective tok/s:** 14.3  
