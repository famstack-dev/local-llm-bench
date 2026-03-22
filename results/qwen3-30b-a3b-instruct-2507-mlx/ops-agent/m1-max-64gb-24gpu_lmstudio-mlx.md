# Apple M1 Max / 64GB / 24 GPU cores

**Model:** qwen3-30b-a3b-instruct-2507-mlx  
**Backend:** lmstudio-mlx  
**Scenario:** ops-agent (conversation)  

| Turn | Context | Prefill | Gen | Gen tok/s | Effective tok/s | Total | Output |
|-----:|--------:|--------:|----:|----------:|----------------:|------:|-------:|
| 1 | 575 | 2.31s | 7.41s | 51.2 | **39.0** | 9.72s | 379 |
| 2 | 1,152 | 1.85s | 10.12s | 48.3 | **40.9** | 11.97s | 489 |
| 3 | 1,710 | 0.95s | 7.04s | 45.0 | **39.7** | 7.99s | 317 |
| 4 | 2,232 | 1.48s | 5.31s | 44.1 | **34.5** | 6.79s | 234 |
| 5 | 2,703 | 1.65s | 11.53s | 41.1 | **36.0** | 13.17s | 474 |
| 6 | 3,378 | 2.12s | 6.50s | 39.5 | **29.8** | 8.62s | 257 |
| 7 | 3,732 | 1.06s | 10.40s | 38.3 | **34.7** | 11.46s | 398 |
| 8 | 4,289 | 1.63s | 13.09s | 35.5 | **31.6** | 14.72s | 465 |

**Total prefill:** 13.0s  
**Total generation:** 71.4s  
**Total time:** 84.4s  
**Avg generation tok/s:** 42.9  
**Avg effective tok/s:** 35.7  
