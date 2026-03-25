# Apple M1 Max / 64GB / 24 GPU cores

**Model:** mlx-community/Qwen3.5-35B-A3B-4bit  
**Backend:** rapid-mlx  
**Scenario:** prefill-test (single-shot)  

| Turn | Context | Prefill | Gen | Gen tok/s | Effective tok/s | Total | Output |
|-----:|--------:|--------:|----:|----------:|----------------:|------:|-------:|
| 1 | 655 | 2.21s | 1.80s | 58.8 | **26.4** | 4.01s | 106 |
| 2 | 1,453 | 4.45s | 2.46s | 61.1 | **21.7** | 6.91s | 150 |
| 3 | 3,015 | 8.85s | 2.48s | 57.7 | **12.6** | 11.33s | 143 |
| 4 | 8,496 | 39.19s | 2.91s | 51.5 | **3.6** | 42.10s | 150 |

**Total prefill:** 54.7s  
**Total generation:** 9.7s  
**Total time:** 64.4s  
**Avg generation tok/s:** 57.3  
**Avg effective tok/s:** 8.5  
