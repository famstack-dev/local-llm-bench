# Apple M1 Max / 64GB / 24 GPU cores

**Model:** Qwen3.5-35B-A3B-4bit  
**Backend:** omlx  
**Scenario:** creative-writing (single-shot)  

| Turn | Context | Prefill | Gen | Gen tok/s | Effective tok/s | Total | Output |
|-----:|--------:|--------:|----:|----------:|----------------:|------:|-------:|
| 1 | 57 | 0.37s | 6.24s | 56.3 | **53.2** | 6.60s | 351 |
| 2 | 60 | 0.37s | 13.70s | 55.7 | **54.2** | 14.07s | 763 |
| 3 | 58 | 0.38s | 5.98s | 56.5 | **53.1** | 6.36s | 338 |

**Total prefill:** 1.1s  
**Total generation:** 25.9s  
**Total time:** 27.0s  
**Avg generation tok/s:** 56.2  
**Avg effective tok/s:** 53.7  
