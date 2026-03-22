# Apple M1 Max / 64GB / 24 GPU cores

**Model:** qwen3:30b (30.5B, Q4_K_M)  
**Backend:** ollama  
**Scenario:** creative-writing (single-shot)  

| Turn | Context | Prefill | Gen | Gen tok/s | Effective tok/s | Total | Output |
|-----:|--------:|--------:|----:|----------:|----------------:|------:|-------:|
| 1 | 57 | 0.36s | 20.69s | 44.8 | **44.0** | 21.05s | 926 |
| 2 | 60 | 0.28s | 18.91s | 45.4 | **44.7** | 19.18s | 858 |
| 3 | 58 | 0.27s | 22.42s | 44.9 | **44.3** | 22.70s | 1006 |

**Total prefill:** 0.9s  
**Total generation:** 62.0s  
**Total time:** 62.9s  
**Avg generation tok/s:** 45.0  
**Avg effective tok/s:** 44.3  
