# Apple M1 Max / 64GB / 24 GPU cores

**Model:** qwen3-30b-a3b-instruct-2507  
**Backend:** lmstudio-gguf  
**Scenario:** creative-writing (single-shot)  

| Turn | Context | Prefill | Gen | Gen tok/s | Effective tok/s | Total | Output |
|-----:|--------:|--------:|----:|----------:|----------------:|------:|-------:|
| 1 | 57 | 0.39s | 9.80s | 57.9 | **55.7** | 10.19s | 568 |
| 2 | 60 | 0.31s | 8.64s | 58.3 | **56.3** | 8.95s | 504 |
| 3 | 58 | 0.31s | 10.27s | 57.9 | **56.2** | 10.57s | 594 |

**Total prefill:** 1.0s  
**Total generation:** 28.7s  
**Total time:** 29.7s  
**Avg generation tok/s:** 58.0  
**Avg effective tok/s:** 56.1  
