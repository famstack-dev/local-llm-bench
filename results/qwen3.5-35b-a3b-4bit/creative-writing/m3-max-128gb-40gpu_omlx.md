# Apple M3 Max / 128GB / 40 GPU cores

**Model:** Qwen3.5-35B-A3B-4bit  
**Backend:** omlx  
**Scenario:** creative-writing (single-shot)  

| Turn | Context | Prefill | Gen | Gen tok/s | Effective tok/s | Total | Output |
|-----:|--------:|--------:|----:|----------:|----------------:|------:|-------:|
| 1 | 57 | 0.39s | 4.49s | 94.6 | **87.1** | 4.88s | 425 |
| 2 | 60 | 0.14s | 6.26s | 93.8 | **91.8** | 6.39s | 587 |
| 3 | 58 | 0.14s | 3.61s | 94.5 | **91.0** | 3.75s | 341 |

**Total prefill:** 0.7s  
**Total generation:** 14.4s  
**Total time:** 15.0s  
**Avg generation tok/s:** 94.3  
**Avg effective tok/s:** 90.1  
