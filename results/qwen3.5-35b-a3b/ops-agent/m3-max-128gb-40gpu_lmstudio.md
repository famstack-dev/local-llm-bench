# Apple M3 Max / 128GB / 40 GPU cores

**Model:** qwen3.5-35b-a3b  
**Backend:** lmstudio  
**Scenario:** ops-agent (conversation)  

| Turn | Context | Prefill | Gen | Gen tok/s | Effective tok/s | Total | Output |
|-----:|--------:|--------:|----:|----------:|----------------:|------:|-------:|
| 1 | 575 | 3.61s | 3.47s | 84.9 | **41.7** | 7.08s | 295 |
| 2 | 1,089 | 4.18s | 3.85s | 83.3 | **40.0** | 8.03s | 321 |
| 3 | 1,516 | 4.53s | 4.38s | 85.6 | **42.1** | 8.91s | 375 |
| 4 | 2,113 | 5.08s | 4.38s | 86.0 | **39.8** | 9.46s | 376 |
| 5 | 2,758 | 5.67s | 5.86s | 81.7 | **41.5** | 11.53s | 479 |
| 6 | 3,440 | 9.05s | 4.60s | 82.7 | **27.9** | 13.64s | 380 |
| 7 | 3,917 | 6.92s | 5.05s | 81.2 | **34.3** | 11.97s | 410 |
| 8 | 4,510 | 7.78s | 5.86s | 82.9 | **35.6** | 13.64s | 486 |

**Total prefill:** 46.8s  
**Total generation:** 37.5s  
**Total time:** 84.3s  
**Avg generation tok/s:** 83.5  
**Avg effective tok/s:** 37.1  
