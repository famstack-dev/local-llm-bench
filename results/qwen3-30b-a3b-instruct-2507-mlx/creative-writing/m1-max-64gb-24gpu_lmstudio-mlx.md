# Apple M1 Max / 64GB / 24 GPU cores

**Model:** qwen3-30b-a3b-instruct-2507-mlx  
**Backend:** lmstudio-mlx  
**Scenario:** creative-writing (single-shot)  

| Turn | Context | Prefill | Gen | Gen tok/s | Effective tok/s | Total | Output |
|-----:|--------:|--------:|----:|----------:|----------------:|------:|-------:|
| 1 | 57 | 0.63s | 13.41s | 55.6 | **53.1** | 14.04s | 746 |
| 2 | 60 | 0.41s | 8.09s | 56.6 | **53.9** | 8.49s | 458 |
| 3 | 58 | 0.38s | 11.15s | 56.0 | **54.2** | 11.53s | 625 |

**Total prefill:** 1.4s  
**Total generation:** 32.6s  
**Total time:** 34.1s  
**Avg generation tok/s:** 56.1  
**Avg effective tok/s:** 53.7  
