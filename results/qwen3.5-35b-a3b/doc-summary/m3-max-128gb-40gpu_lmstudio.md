# Apple M3 Max / 128GB / 40 GPU cores

**Model:** qwen3.5-35b-a3b  
**Backend:** lmstudio  
**Scenario:** doc-summary (single-shot)  

| Turn | Context | Prefill | Gen | Gen tok/s | Effective tok/s | Total | Output |
|-----:|--------:|--------:|----:|----------:|----------------:|------:|-------:|
| 1 | 425 | 3.45s | 1.21s | 88.9 | **23.1** | 4.67s | 108 |
| 2 | 612 | 3.29s | 1.05s | 87.5 | **21.2** | 4.34s | 92 |
| 3 | 535 | 3.40s | 1.37s | 87.6 | **25.1** | 4.77s | 120 |
| 4 | 524 | 3.37s | 1.22s | 86.1 | **22.9** | 4.59s | 105 |
| 5 | 1,518 | 4.34s | 1.34s | 86.3 | **20.4** | 5.68s | 116 |

**Total prefill:** 17.9s  
**Total generation:** 6.2s  
**Total time:** 24.1s  
**Avg generation tok/s:** 87.3  
**Avg effective tok/s:** 22.5  
