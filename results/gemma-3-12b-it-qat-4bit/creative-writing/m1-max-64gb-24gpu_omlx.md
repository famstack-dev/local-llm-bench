# Apple M1 Max / 64GB / 24 GPU cores

**Model:** gemma-3-12b-it-qat-4bit  
**Backend:** omlx  
**Scenario:** creative-writing (single-shot)  

| Turn | Context | Prefill | Gen | Gen tok/s | Effective tok/s | Total | Output |
|-----:|--------:|--------:|----:|----------:|----------------:|------:|-------:|
| 1 | 57 | 0.55s | 12.73s | 27.5 | **26.3** | 13.29s | 350 |
| 2 | 60 | 0.59s | 15.33s | 27.4 | **26.4** | 15.92s | 420 |
| 3 | 58 | 0.60s | 13.68s | 27.5 | **26.3** | 14.28s | 376 |

**Total prefill:** 1.7s  
**Total generation:** 41.7s  
**Total time:** 43.5s  
**Avg generation tok/s:** 27.5  
**Avg effective tok/s:** 26.4  
