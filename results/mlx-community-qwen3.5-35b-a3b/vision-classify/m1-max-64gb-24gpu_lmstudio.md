# Apple M1 Max / 64GB / 24 GPU cores

**Model:** mlx-community/qwen3.5-35b-a3b  
**Backend:** lmstudio  
**Scenario:** vision-classify (single-shot)  

| Turn | Context | Prefill | Gen | Gen tok/s | Effective tok/s | Total | Output |
|-----:|--------:|--------:|----:|----------:|----------------:|------:|-------:|
| 1 | 1,136 | 10.80s | 1.68s | 53.7 | **7.2** | 12.48s | 90 |
| 2 | 1,136 | 16.29s | 1.46s | 55.3 | **4.6** | 17.75s | 81 |
| 3 | 1,136 | 11.40s | 1.45s | 55.7 | **6.3** | 12.85s | 81 |
| 4 | 1,136 | 10.49s | 1.45s | 55.9 | **6.8** | 11.94s | 81 |
| 5 | 1,136 | 7.81s | 1.27s | 55.2 | **7.7** | 9.08s | 70 |
| 6 | 1,136 | 7.89s | 1.01s | 55.2 | **6.3** | 8.90s | 56 |
| 7 | 1,136 | 15.57s | 1.34s | 55.3 | **4.4** | 16.91s | 74 |
| 8 | 1,136 | 7.67s | 1.39s | 54.9 | **8.4** | 9.05s | 76 |

**Total prefill:** 87.9s  
**Total generation:** 11.0s  
**Total time:** 99.0s  
**Avg generation tok/s:** 55.1  
**Avg effective tok/s:** 6.2  
