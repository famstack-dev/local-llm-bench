# Apple M1 Max / 64GB / 24 GPU cores

**Model:** mlx-community/qwen3.5-35b-a3b  
**Backend:** lmstudio  
**Scenario:** vision-extract (single-shot)  

| Turn | Context | Prefill | Gen | Gen tok/s | Effective tok/s | Total | Output |
|-----:|--------:|--------:|----:|----------:|----------------:|------:|-------:|
| 1 | 1,078 | 10.49s | 3.45s | 54.2 | **13.4** | 13.94s | 187 |
| 2 | 1,078 | 15.72s | 7.55s | 53.4 | **17.3** | 23.26s | 403 |
| 3 | 1,078 | 11.08s | 11.62s | 53.7 | **27.5** | 22.70s | 624 |
| 4 | 1,078 | 10.32s | 10.22s | 53.3 | **26.5** | 20.54s | 545 |
| 5 | 1,078 | 7.75s | 3.19s | 56.7 | **16.5** | 10.94s | 181 |
| 6 | 1,078 | 7.58s | 8.78s | 54.9 | **29.5** | 16.36s | 482 |
| 7 | 1,078 | 15.06s | 8.82s | 51.9 | **19.2** | 23.88s | 458 |
| 8 | 1,078 | 7.54s | 7.58s | 53.7 | **26.9** | 15.12s | 407 |

**Total prefill:** 85.5s  
**Total generation:** 61.2s  
**Total time:** 146.7s  
**Avg generation tok/s:** 54.0  
**Avg effective tok/s:** 22.4  
