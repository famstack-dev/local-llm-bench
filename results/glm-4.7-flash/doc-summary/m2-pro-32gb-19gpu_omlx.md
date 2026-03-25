# Apple M2 Pro / 32GB / 19 GPU cores

**Model:** GLM-4.7-Flash-4bit  
**Backend:** omlx  
**Scenario:** doc-summary (single-shot)  

| Turn | Context | Prefill | Gen | Gen tok/s | Effective tok/s | Total | Output |
|-----:|--------:|--------:|----:|----------:|----------------:|------:|-------:|
| 1 | 425 | 1.97s | 1.40s | 39.2 | **16.3** | 3.37s | 55 |
| 2 | 612 | 2.06s | 1.52s | 39.4 | **16.8** | 3.58s | 60 |
| 3 | 535 | 2.26s | 1.68s | 40.0 | **17.0** | 3.93s | 67 |
| 4 | 524 | 2.15s | 1.72s | 39.4 | **17.5** | 3.88s | 68 |
| 5 | 1,518 | 5.47s | 2.72s | 37.5 | **12.5** | 8.19s | 102 |

**Total prefill:** 13.9s  
**Total generation:** 9.0s  
**Total time:** 22.9s  
**Avg generation tok/s:** 39.1  
**Avg effective tok/s:** 15.3  
