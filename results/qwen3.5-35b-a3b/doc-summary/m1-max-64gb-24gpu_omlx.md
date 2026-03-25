# Apple M1 Max / 64GB / 24 GPU cores

**Model:** Qwen3.5-35B-A3B-4bit  
**Backend:** omlx  
**Scenario:** doc-summary (single-shot)  

| Turn | Context | Prefill | Gen | Gen tok/s | Effective tok/s | Total | Output |
|-----:|--------:|--------:|----:|----------:|----------------:|------:|-------:|
| 1 | 425 | 1.61s | 2.03s | 55.8 | **31.1** | 3.64s | 113 |
| 2 | 612 | 1.51s | 1.64s | 55.7 | **28.9** | 3.15s | 91 |
| 3 | 535 | 1.72s | 1.77s | 55.4 | **28.1** | 3.49s | 98 |
| 4 | 524 | 1.64s | 1.82s | 55.5 | **29.2** | 3.46s | 101 |
| 5 | 1,518 | 1.74s | 2.05s | 55.2 | **29.8** | 3.79s | 113 |

**Total prefill:** 8.2s  
**Total generation:** 9.3s  
**Total time:** 17.5s  
**Avg generation tok/s:** 55.5  
**Avg effective tok/s:** 29.4  
