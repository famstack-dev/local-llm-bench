# Apple M1 Max / 64GB / 24 GPU cores

**Model:** Qwen3.6-35B-A3B-UD-MLX-4bit  
**Backend:** omlx  
**Scenario:** vision-classify (single-shot)  

| Turn | Context | Prefill | Gen | Gen tok/s | Effective tok/s | Total | Output |
|-----:|--------:|--------:|----:|----------:|----------------:|------:|-------:|
| 1 | 1,136 | 5.33s | 1.79s | 49.2 | **12.4** | 7.12s | 88 |
| 2 | 1,136 | 9.89s | 1.84s | 47.3 | **7.4** | 11.73s | 87 |
| 3 | 1,136 | 5.79s | 1.80s | 48.8 | **11.6** | 7.60s | 88 |
| 4 | 1,136 | 19.62s | 1.89s | 46.5 | **4.1** | 21.51s | 88 |
| 5 | 1,136 | 3.07s | 1.58s | 48.7 | **16.6** | 4.65s | 77 |
| 6 | 1,136 | 3.04s | 1.30s | 48.5 | **14.5** | 4.33s | 63 |
| 7 | 1,136 | 9.90s | 1.85s | 47.6 | **7.5** | 11.75s | 88 |
| 8 | 1,136 | 2.96s | 1.69s | 48.6 | **17.6** | 4.65s | 82 |

**Total prefill:** 59.6s  
**Total generation:** 13.7s  
**Total time:** 73.3s  
**Avg generation tok/s:** 48.1  
**Avg effective tok/s:** 9.0  
