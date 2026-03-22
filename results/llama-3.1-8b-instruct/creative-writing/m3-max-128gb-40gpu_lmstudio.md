# Apple M3 Max / 128GB / 40 GPU cores

**Model:** llama-3.1-8b-instruct  
**Backend:** lmstudio  
**Scenario:** creative-writing (single-shot)  

| Turn | Context | Prefill | Gen | Gen tok/s | Effective tok/s | Total | Output |
|-----:|--------:|--------:|----:|----------:|----------------:|------:|-------:|
| 1 | 57 | 0.52s | 12.77s | 24.0 | **23.1** | 13.29s | 307 |
| 2 | 60 | 0.42s | 13.14s | 24.2 | **23.4** | 13.57s | 318 |
| 3 | 58 | 0.39s | 12.91s | 24.2 | **23.5** | 13.30s | 313 |

**Total prefill:** 1.3s  
**Total generation:** 38.8s  
**Total time:** 40.1s  
**Avg generation tok/s:** 24.1  
**Avg effective tok/s:** 23.4  
