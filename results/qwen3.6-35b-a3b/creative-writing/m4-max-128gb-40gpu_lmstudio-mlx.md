# Apple M4 Max / 128GB / 40 GPU cores

**Model:** qwen3.6-35b-a3b  
**Backend:** lmstudio-mlx  
**Scenario:** creative-writing (single-shot)  

| Turn | Context | Prefill | Gen | Gen tok/s | Effective tok/s | Total | Output |
|-----:|--------:|--------:|----:|----------:|----------------:|------:|-------:|
| 1 | 57 | 0.42s | 5.12s | 89.8 | **83.0** | 5.54s | 460 |
| 2 | 60 | 0.29s | 8.42s | 91.7 | **88.6** | 8.71s | 772 |
| 3 | 58 | 0.30s | 5.21s | 93.3 | **88.1** | 5.51s | 486 |

**Total prefill:** 1.0s  
**Total generation:** 18.8s  
**Total time:** 19.8s  
**Avg generation tok/s:** 91.6  
**Avg effective tok/s:** 86.9  
