# Apple M3 Max / 128GB / 40 GPU cores

**Model:** qwen3.5-35b-a3b  
**Backend:** lmstudio  
**Scenario:** creative-writing (single-shot)  

| Turn | Context | Prefill | Gen | Gen tok/s | Effective tok/s | Total | Output |
|-----:|--------:|--------:|----:|----------:|----------------:|------:|-------:|
| 1 | 57 | 2.95s | 4.37s | 94.3 | **56.3** | 7.32s | 412 |
| 2 | 60 | 2.92s | 7.53s | 91.5 | **65.9** | 10.45s | 689 |
| 3 | 58 | 2.92s | 3.80s | 90.7 | **51.3** | 6.72s | 345 |

**Total prefill:** 8.8s  
**Total generation:** 15.7s  
**Total time:** 24.5s  
**Avg generation tok/s:** 92.2  
**Avg effective tok/s:** 59.0  
