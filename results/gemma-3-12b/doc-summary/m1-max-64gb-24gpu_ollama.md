# Apple M1 Max / 64GB / 24 GPU cores

**Model:** gemma3:12b-it-qat (12.2B, Q4_0)  
**Backend:** ollama  
**Scenario:** doc-summary (single-shot)  

| Turn | Context | Prefill | Gen | Gen tok/s | Effective tok/s | Total | Output |
|-----:|--------:|--------:|----:|----------:|----------------:|------:|-------:|
| 1 | 425 | 2.57s | 5.01s | 20.7 | **13.7** | 7.58s | 104 |
| 2 | 612 | 1.92s | 5.04s | 20.6 | **14.9** | 6.96s | 104 |
| 3 | 535 | 2.17s | 4.29s | 21.7 | **14.4** | 6.46s | 93 |
| 4 | 524 | 2.15s | 5.79s | 20.6 | **15.0** | 7.93s | 119 |
| 5 | 1,518 | 6.68s | 5.30s | 17.7 | **7.8** | 11.98s | 94 |

**Total prefill:** 15.5s  
**Total generation:** 25.4s  
**Total time:** 40.9s  
**Avg generation tok/s:** 20.3  
**Avg effective tok/s:** 12.6  
