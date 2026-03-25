# Apple M1 Max / 64GB / 24 GPU cores

**Model:** qwen/qwen2.5-vl-7b  
**Backend:** lmstudio  
**Scenario:** vision-extract (single-shot)  

| Turn | Context | Prefill | Gen | Gen tok/s | Effective tok/s | Total | Output |
|-----:|--------:|--------:|----:|----------:|----------------:|------:|-------:|
| 1 | 1,078 | 9.36s | 5.00s | 41.4 | **14.4** | 14.36s | 207 |
| 2 | 1,078 | 15.91s | 9.65s | 37.9 | **14.3** | 25.56s | 366 |
| 3 | 1,078 | 10.05s | 11.66s | 39.4 | **21.1** | 21.71s | 459 |
| 4 | 1,078 | 8.62s | 14.51s | 38.4 | **24.1** | 23.12s | 557 |
| 5 | 1,078 | 4.97s | 4.10s | 40.7 | **18.4** | 9.07s | 167 |
| 6 | 1,078 | 4.86s | 13.33s | 39.8 | **29.1** | 18.19s | 530 |
| 7 | 1,078 | 15.07s | 7.87s | 40.1 | **13.7** | 22.93s | 315 |
| 8 | 1,078 | 4.46s | 11.30s | 40.6 | **29.1** | 15.76s | 459 |

**Total prefill:** 73.3s  
**Total generation:** 77.4s  
**Total time:** 150.7s  
**Avg generation tok/s:** 39.8  
**Avg effective tok/s:** 20.3  
