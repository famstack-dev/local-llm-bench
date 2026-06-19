# Apple M4 Max / 128GB / 40 GPU cores

**Model:** gemma-4-e4b-it-mlx  
**Backend:** lmstudio  
**Scenario:** prefill-test (single-shot)  

| Turn | Context | Prefill | Gen | Gen tok/s | Effective tok/s | Total | Output |
|-----:|--------:|--------:|----:|----------:|----------------:|------:|-------:|
| 1 | 655 | 0.60s | 1.53s | 72.3 | **52.0** | 2.14s | 111 |
| 2 | 1,453 | 0.95s | 1.90s | 71.5 | **47.7** | 2.85s | 136 |
| 3 | 3,015 | 1.93s | 2.08s | 69.7 | **36.1** | 4.01s | 145 |
| 4 | 8,496 | 7.26s | 2.33s | 63.9 | **15.5** | 9.59s | 149 |

**Total prefill:** 10.7s  
**Total generation:** 7.8s  
**Total time:** 18.6s  
**Avg generation tok/s:** 69.3  
**Avg effective tok/s:** 29.1  
