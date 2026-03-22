# Apple M1 Max / 64GB / 24 GPU cores

**Model:** qwen3-30b-a3b-instruct-2507  
**Backend:** lmstudio-gguf  
**Scenario:** doc-summary (single-shot)  

| Turn | Context | Prefill | Gen | Gen tok/s | Effective tok/s | Total | Output |
|-----:|--------:|--------:|----:|----------:|----------------:|------:|-------:|
| 1 | 425 | 1.17s | 1.93s | 50.8 | **31.7** | 3.09s | 98 |
| 2 | 612 | 0.80s | 1.37s | 59.1 | **37.3** | 2.17s | 81 |
| 3 | 535 | 0.90s | 1.77s | 58.7 | **38.9** | 2.67s | 104 |
| 4 | 524 | 0.86s | 2.42s | 57.9 | **42.7** | 3.28s | 140 |
| 5 | 1,518 | 2.96s | 2.65s | 54.6 | **25.8** | 5.61s | 145 |

**Total prefill:** 6.7s  
**Total generation:** 10.1s  
**Total time:** 16.8s  
**Avg generation tok/s:** 56.2  
**Avg effective tok/s:** 33.7  
