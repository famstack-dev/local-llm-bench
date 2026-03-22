# Apple M1 Max / 64GB / 24 GPU cores

**Model:** qwen/qwen3-vl-8b  
**Backend:** lmstudio  
**Scenario:** vision-extract (single-shot)  

| Turn | Context | Prefill | Gen | Gen tok/s | Effective tok/s | Total | Output |
|-----:|--------:|--------:|----:|----------:|----------------:|------:|-------:|
| 1 | 1,078 | 12.05s | 4.79s | 40.3 | **11.5** | 16.84s | 193 |
| 2 | 1,078 | 19.09s | 8.24s | 38.2 | **11.5** | 27.32s | 315 |
| 3 | 1,078 | 12.34s | 16.81s | 39.4 | **22.7** | 29.15s | 663 |
| 4 | 1,078 | 11.12s | 12.50s | 40.4 | **21.4** | 23.62s | 505 |
| 5 | 1,078 | 7.14s | 4.15s | 44.1 | **16.2** | 11.29s | 183 |
| 6 | 1,078 | 7.27s | 11.90s | 42.6 | **26.4** | 19.17s | 507 |
| 7 | 1,078 | 18.95s | 9.38s | 36.5 | **12.1** | 28.33s | 342 |
| 8 | 1,078 | 7.11s | 8.37s | 42.7 | **23.1** | 15.48s | 357 |

**Total prefill:** 95.1s  
**Total generation:** 76.1s  
**Total time:** 171.2s  
**Avg generation tok/s:** 40.5  
**Avg effective tok/s:** 17.9  
