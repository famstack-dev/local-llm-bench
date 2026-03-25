# Apple M1 Max / 64GB / 24 GPU cores

**Model:** qwen/qwen3.5-35b-a3b  
**Backend:** lmstudio  
**Scenario:** creative-writing (single-shot)  

| Turn | Context | Prefill | Gen | Gen tok/s | Effective tok/s | Total | Output |
|-----:|--------:|--------:|----:|----------:|----------------:|------:|-------:|
| 1 | 57 | 0.56s | 13.90s | 28.7 | **27.6** | 14.46s | 399 |
| 2 | 60 | 0.53s | 23.56s | 28.5 | **27.9** | 24.09s | 672 |
| 3 | 58 | 0.55s | 14.64s | 28.7 | **27.7** | 15.19s | 420 |

**Total prefill:** 1.6s  
**Total generation:** 52.1s  
**Total time:** 53.7s  
**Avg generation tok/s:** 28.6  
**Avg effective tok/s:** 27.7  
