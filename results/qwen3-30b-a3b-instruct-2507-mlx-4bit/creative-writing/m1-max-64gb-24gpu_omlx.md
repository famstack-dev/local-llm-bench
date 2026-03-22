# Apple M1 Max / 64GB / 24 GPU cores

**Model:** Qwen3-30B-A3B-Instruct-2507-MLX-4bit  
**Backend:** omlx  
**Scenario:** creative-writing (single-shot)  

| Turn | Context | Prefill | Gen | Gen tok/s | Effective tok/s | Total | Output |
|-----:|--------:|--------:|----:|----------:|----------------:|------:|-------:|
| 1 | 57 | 0.65s | 12.13s | 55.6 | **52.8** | 12.78s | 675 |
| 2 | 60 | 0.63s | 9.41s | 56.2 | **52.7** | 10.04s | 529 |
| 3 | 58 | 0.67s | 13.00s | 55.5 | **52.8** | 13.68s | 722 |

**Total prefill:** 2.0s  
**Total generation:** 34.5s  
**Total time:** 36.5s  
**Avg generation tok/s:** 55.8  
**Avg effective tok/s:** 52.8  
