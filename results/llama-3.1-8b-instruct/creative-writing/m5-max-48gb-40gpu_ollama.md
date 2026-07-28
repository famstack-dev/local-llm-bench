# Apple M5 Max / 48GB / 40 GPU cores

**Model:** llama3.1:8b (8.0B, Q4_K_M)  
**Backend:** ollama  
**Scenario:** creative-writing (single-shot)  

| Turn | Context | Prefill | Gen | Gen tok/s | Effective tok/s | Total | Output |
|-----:|--------:|--------:|----:|----------:|----------------:|------:|-------:|
| 1 | 57 | 0.15s | 3.84s | 88.8 | **85.5** | 3.99s | 341 |
| 2 | 60 | 0.15s | 4.24s | 84.9 | **82.0** | 4.39s | 360 |
| 3 | 58 | 0.15s | 3.54s | 82.0 | **78.6** | 3.69s | 290 |

**Total prefill:** 0.4s  
**Total generation:** 11.6s  
**Total time:** 12.1s  
**Avg generation tok/s:** 85.2  
**Avg effective tok/s:** 82.1  
