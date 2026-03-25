# Apple M1 Max / 64GB / 24 GPU cores

**Model:** qwen/qwen3.5-35b-a3b  
**Backend:** lmstudio  
**Scenario:** ops-agent (conversation)  

| Turn | Context | Prefill | Gen | Gen tok/s | Effective tok/s | Total | Output |
|-----:|--------:|--------:|----:|----------:|----------------:|------:|-------:|
| 1 | 575 | 2.03s | 10.90s | 28.6 | **24.1** | 12.93s | 312 |
| 2 | 1,117 | 3.78s | 11.68s | 28.0 | **21.2** | 15.46s | 327 |
| 3 | 1,522 | 4.91s | 9.41s | 28.5 | **18.7** | 14.32s | 268 |
| 4 | 2,019 | 6.05s | 9.87s | 28.3 | **17.5** | 15.92s | 279 |
| 5 | 2,557 | 7.35s | 15.85s | 27.8 | **19.0** | 23.20s | 441 |
| 6 | 3,243 | 9.45s | 8.99s | 28.1 | **13.7** | 18.44s | 253 |
| 7 | 3,607 | 10.55s | 10.89s | 28.1 | **14.3** | 21.45s | 306 |
| 8 | 4,111 | 12.06s | 16.13s | 28.0 | **16.0** | 28.20s | 451 |

**Total prefill:** 56.2s  
**Total generation:** 93.7s  
**Total time:** 149.9s  
**Avg generation tok/s:** 28.2  
**Avg effective tok/s:** 17.6  
