# Apple M1 Max / 64GB / 24 GPU cores

**Model:** mistral-small-3.1-24b-instruct-2503  
**Backend:** lmstudio  
**Scenario:** vision-classify (single-shot)  

| Turn | Context | Prefill | Gen | Gen tok/s | Effective tok/s | Total | Output |
|-----:|--------:|--------:|----:|----------:|----------------:|------:|-------:|
| 1 | 1,136 | 13.12s | 5.14s | 15.9 | **4.5** | 18.26s | 82 |
| 2 | 1,136 | 12.81s | 6.51s | 15.7 | **5.3** | 19.32s | 102 |
| 3 | 1,136 | 12.40s | 4.00s | 16.5 | **4.0** | 16.41s | 66 |
| 4 | 1,136 | 13.22s | 5.07s | 15.8 | **4.4** | 18.29s | 80 |
| 5 | 1,136 | 12.41s | 4.33s | 16.2 | **4.2** | 16.74s | 70 |
| 6 | 1,136 | 11.76s | 3.31s | 16.6 | **3.7** | 15.07s | 55 |
| 7 | 1,136 | 12.41s | 4.06s | 16.0 | **3.9** | 16.47s | 65 |
| 8 | 1,136 | 10.89s | 3.78s | 16.7 | **4.3** | 14.68s | 63 |

**Total prefill:** 99.0s  
**Total generation:** 36.2s  
**Total time:** 135.2s  
**Avg generation tok/s:** 16.2  
**Avg effective tok/s:** 4.3  
