# Apple M1 Max / 64GB / 24 GPU cores

**Model:** qwen/qwen2.5-vl-7b  
**Backend:** lmstudio  
**Scenario:** vision-classify (single-shot)  

| Turn | Context | Prefill | Gen | Gen tok/s | Effective tok/s | Total | Output |
|-----:|--------:|--------:|----:|----------:|----------------:|------:|-------:|
| 1 | 1,136 | 9.39s | 2.06s | 42.1 | **7.6** | 11.46s | 87 |
| 2 | 1,136 | 16.26s | 1.65s | 42.3 | **3.9** | 17.91s | 70 |
| 3 | 1,136 | 9.72s | 1.80s | 42.7 | **6.7** | 11.52s | 77 |
| 4 | 1,136 | 8.53s | 2.05s | 42.0 | **8.1** | 10.58s | 86 |
| 5 | 1,136 | 5.00s | 1.45s | 44.7 | **10.1** | 6.45s | 65 |
| 6 | 1,136 | 4.84s | 1.11s | 46.7 | **8.7** | 5.96s | 52 |
| 7 | 1,136 | 15.16s | 1.99s | 42.3 | **4.9** | 17.15s | 84 |
| 8 | 1,136 | 4.58s | 1.41s | 44.8 | **10.5** | 5.99s | 63 |

**Total prefill:** 73.5s  
**Total generation:** 13.5s  
**Total time:** 87.0s  
**Avg generation tok/s:** 43.5  
**Avg effective tok/s:** 6.7  
