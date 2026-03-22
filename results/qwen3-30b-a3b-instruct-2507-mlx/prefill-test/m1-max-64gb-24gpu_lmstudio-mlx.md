# Apple M1 Max / 64GB / 24 GPU cores

**Model:** qwen3-30b-a3b-instruct-2507-mlx  
**Backend:** lmstudio-mlx  
**Scenario:** prefill-test (single-shot)  

| Turn | Context | Prefill | Gen | Gen tok/s | Effective tok/s | Total | Output |
|-----:|--------:|--------:|----:|----------:|----------------:|------:|-------:|
| 1 | 655 | 2.50s | 2.40s | 54.1 | **26.5** | 4.90s | 130 |
| 2 | 1,453 | 4.77s | 2.98s | 49.0 | **18.8** | 7.75s | 146 |
| 3 | 3,015 | 11.14s | 3.38s | 44.1 | **10.3** | 14.53s | 149 |
| 4 | 8,496 | 62.46s | 5.56s | 26.4 | **2.2** | 68.02s | 147 |

**Total prefill:** 80.9s  
**Total generation:** 14.3s  
**Total time:** 95.2s  
**Avg generation tok/s:** 43.4  
**Avg effective tok/s:** 6.0  
