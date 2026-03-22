# Apple M1 Max / 64GB / 24 GPU cores

**Model:** gemma3:12b-it-qat (12.2B, Q4_0)  
**Backend:** ollama  
**Scenario:** creative-writing (single-shot)  

| Turn | Context | Prefill | Gen | Gen tok/s | Effective tok/s | Total | Output |
|-----:|--------:|--------:|----:|----------:|----------------:|------:|-------:|
| 1 | 57 | 0.50s | 14.12s | 24.1 | **23.3** | 14.62s | 340 |
| 2 | 60 | 0.37s | 14.77s | 24.0 | **23.4** | 15.14s | 354 |
| 3 | 58 | 0.39s | 12.39s | 23.7 | **22.9** | 12.78s | 293 |

**Total prefill:** 1.3s  
**Total generation:** 41.3s  
**Total time:** 42.5s  
**Avg generation tok/s:** 23.9  
**Avg effective tok/s:** 23.2  
