# Apple M1 Max / 64GB / 24 GPU cores

**Model:** Qwen3-30B-A3B-Instruct-2507-MLX-4bit  
**Backend:** omlx  
**Scenario:** prefill-test (single-shot)  

| Turn | Context | Prefill | Gen | Gen tok/s | Effective tok/s | Total | Output |
|-----:|--------:|--------:|----:|----------:|----------------:|------:|-------:|
| 1 | 655 | 2.47s | 2.65s | 51.4 | **26.6** | 5.12s | 136 |
| 2 | 1,453 | 4.95s | 3.14s | 45.5 | **17.7** | 8.09s | 143 |
| 3 | 3,015 | 11.23s | 3.68s | 40.5 | **10.0** | 14.90s | 149 |
| 4 | 8,496 | 62.28s | 6.51s | 22.6 | **2.1** | 68.80s | 147 |

**Total prefill:** 80.9s  
**Total generation:** 16.0s  
**Total time:** 96.9s  
**Avg generation tok/s:** 40.0  
**Avg effective tok/s:** 5.9  
