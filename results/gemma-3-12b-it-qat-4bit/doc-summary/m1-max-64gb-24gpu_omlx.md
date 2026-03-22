# Apple M1 Max / 64GB / 24 GPU cores

**Model:** gemma-3-12b-it-qat-4bit  
**Backend:** omlx  
**Scenario:** doc-summary (single-shot)  

| Turn | Context | Prefill | Gen | Gen tok/s | Effective tok/s | Total | Output |
|-----:|--------:|--------:|----:|----------:|----------------:|------:|-------:|
| 1 | 425 | 3.91s | 3.72s | 25.8 | **12.6** | 7.63s | 96 |
| 2 | 612 | 3.86s | 3.42s | 25.4 | **11.9** | 7.28s | 87 |
| 3 | 535 | 4.30s | 3.72s | 25.5 | **11.8** | 8.02s | 95 |
| 4 | 524 | 4.12s | 4.08s | 26.0 | **12.9** | 8.19s | 106 |
| 5 | 1,518 | 4.52s | 5.72s | 26.2 | **14.6** | 10.25s | 150 |

**Total prefill:** 20.7s  
**Total generation:** 20.7s  
**Total time:** 41.4s  
**Avg generation tok/s:** 25.8  
**Avg effective tok/s:** 12.9  
