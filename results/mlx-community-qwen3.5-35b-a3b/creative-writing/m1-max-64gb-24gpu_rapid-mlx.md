# Apple M1 Max / 64GB / 24 GPU cores

**Model:** mlx-community/Qwen3.5-35B-A3B-4bit  
**Backend:** rapid-mlx  
**Scenario:** creative-writing (single-shot)  

| Turn | Context | Prefill | Gen | Gen tok/s | Effective tok/s | Total | Output |
|-----:|--------:|--------:|----:|----------:|----------------:|------:|-------:|
| 1 | 57 | 0.73s | 6.48s | 62.3 | **56.0** | 7.21s | 404 |
| 2 | 60 | 0.62s | 6.17s | 62.1 | **56.4** | 6.79s | 383 |
| 3 | 58 | 0.42s | 4.80s | 62.3 | **57.3** | 5.21s | 299 |

**Total prefill:** 1.8s  
**Total generation:** 17.4s  
**Total time:** 19.2s  
**Avg generation tok/s:** 62.2  
**Avg effective tok/s:** 56.5  
