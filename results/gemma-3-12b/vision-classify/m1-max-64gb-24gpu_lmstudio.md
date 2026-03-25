# Apple M1 Max / 64GB / 24 GPU cores

**Model:** google/gemma-3-12b  
**Backend:** lmstudio  
**Scenario:** vision-classify (single-shot)  

| Turn | Context | Prefill | Gen | Gen tok/s | Effective tok/s | Total | Output |
|-----:|--------:|--------:|----:|----------:|----------------:|------:|-------:|
| 1 | 1,136 | 4.92s | 2.78s | 30.2 | **10.9** | 7.70s | 84 |
| 2 | 1,136 | 5.08s | 2.93s | 30.0 | **11.0** | 8.01s | 88 |
| 3 | 1,136 | 5.00s | 2.71s | 30.3 | **10.6** | 7.71s | 82 |
| 4 | 1,136 | 5.46s | 3.19s | 29.7 | **11.0** | 8.65s | 95 |
| 5 | 1,136 | 4.89s | 2.64s | 30.3 | **10.6** | 7.53s | 80 |
| 6 | 1,136 | 4.91s | 2.01s | 31.3 | **9.1** | 6.92s | 63 |
| 7 | 1,136 | 4.98s | 2.50s | 30.4 | **10.2** | 7.48s | 76 |
| 8 | 1,136 | 4.93s | 2.60s | 30.4 | **10.5** | 7.53s | 79 |

**Total prefill:** 40.2s  
**Total generation:** 21.4s  
**Total time:** 61.5s  
**Avg generation tok/s:** 30.3  
**Avg effective tok/s:** 10.5  
