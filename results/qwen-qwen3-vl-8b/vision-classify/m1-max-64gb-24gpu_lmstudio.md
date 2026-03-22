# Apple M1 Max / 64GB / 24 GPU cores

**Model:** qwen/qwen3-vl-8b  
**Backend:** lmstudio  
**Scenario:** vision-classify (single-shot)  

| Turn | Context | Prefill | Gen | Gen tok/s | Effective tok/s | Total | Output |
|-----:|--------:|--------:|----:|----------:|----------------:|------:|-------:|
| 1 | 1,136 | 12.02s | 2.00s | 41.0 | **5.8** | 14.02s | 82 |
| 2 | 1,136 | 19.56s | 1.75s | 39.9 | **3.3** | 21.31s | 70 |
| 3 | 1,136 | 12.76s | 1.82s | 41.3 | **5.1** | 14.58s | 75 |
| 4 | 1,136 | 11.47s | 1.85s | 41.6 | **5.8** | 13.32s | 77 |
| 5 | 1,136 | 7.69s | 1.41s | 42.4 | **6.6** | 9.11s | 60 |
| 6 | 1,136 | 7.68s | 1.05s | 41.9 | **5.0** | 8.73s | 44 |
| 7 | 1,136 | 19.41s | 2.11s | 40.2 | **3.9** | 21.52s | 85 |
| 8 | 1,136 | 7.48s | 1.30s | 42.4 | **6.3** | 8.78s | 55 |

**Total prefill:** 98.1s  
**Total generation:** 13.3s  
**Total time:** 111.4s  
**Avg generation tok/s:** 41.3  
**Avg effective tok/s:** 4.9  
