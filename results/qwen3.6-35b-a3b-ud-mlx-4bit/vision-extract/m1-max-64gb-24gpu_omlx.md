# Apple M1 Max / 64GB / 24 GPU cores

**Model:** Qwen3.6-35B-A3B-UD-MLX-4bit  
**Backend:** omlx  
**Scenario:** vision-extract (single-shot)  

| Turn | Context | Prefill | Gen | Gen tok/s | Effective tok/s | Total | Output |
|-----:|--------:|--------:|----:|----------:|----------------:|------:|-------:|
| 1 | 1,078 | 3.42s | 3.52s | 48.6 | **24.7** | 6.93s | 171 |
| 2 | 1,078 | 5.86s | 7.79s | 49.4 | **28.2** | 13.64s | 385 |
| 3 | 1,078 | 3.47s | 13.23s | 50.2 | **39.8** | 16.70s | 664 |
| 4 | 1,078 | 9.18s | 10.49s | 48.5 | **25.9** | 19.67s | 509 |
| 5 | 1,078 | 2.12s | 2.79s | 49.4 | **28.1** | 4.91s | 138 |
| 6 | 1,078 | 2.06s | 10.00s | 50.3 | **41.7** | 12.06s | 503 |
| 7 | 1,078 | 5.53s | 10.95s | 49.7 | **33.0** | 16.48s | 544 |
| 8 | 1,078 | 1.97s | 8.51s | 50.6 | **41.1** | 10.48s | 431 |

**Total prefill:** 33.6s  
**Total generation:** 67.3s  
**Total time:** 100.9s  
**Avg generation tok/s:** 49.6  
**Avg effective tok/s:** 33.2  
