# Apple M3 Max / 128GB / 40 GPU cores

**Model:** llama-3.1-8b-instruct  
**Backend:** lmstudio  
**Scenario:** creative-writing (single-shot)  

| Turn | Context | Prefill | Gen | Gen tok/s | Effective tok/s | Total | Output |
|-----:|--------:|--------:|----:|----------:|----------------:|------:|-------:|
| 1 | 57 | 0.23s | 5.15s | 78.1 | **74.8** | 5.38s | 402 |
| 2 | 60 | 0.19s | 5.01s | 78.4 | **75.5** | 5.21s | 393 |
| 3 | 58 | 0.19s | 3.83s | 79.0 | **75.3** | 4.03s | 303 |

**Total prefill:** 0.6s  
**Total generation:** 14.0s  
**Total time:** 14.6s  
**Avg generation tok/s:** 78.5  
**Avg effective tok/s:** 75.2  
