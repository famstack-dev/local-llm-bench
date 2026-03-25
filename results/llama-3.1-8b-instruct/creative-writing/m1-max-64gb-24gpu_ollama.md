# Apple M1 Max / 64GB / 24 GPU cores

**Model:** llama3.1:8b (8.0B, Q4_K_M)  
**Backend:** ollama  
**Scenario:** creative-writing (single-shot)  

| Turn | Context | Prefill | Gen | Gen tok/s | Effective tok/s | Total | Output |
|-----:|--------:|--------:|----:|----------:|----------------:|------:|-------:|
| 1 | 57 | 0.39s | 11.23s | 39.5 | **38.2** | 11.62s | 444 |
| 2 | 60 | 0.18s | 11.88s | 39.5 | **38.9** | 12.07s | 469 |
| 3 | 58 | 0.18s | 7.58s | 39.8 | **38.9** | 7.77s | 302 |

**Total prefill:** 0.8s  
**Total generation:** 30.7s  
**Total time:** 31.5s  
**Avg generation tok/s:** 39.6  
**Avg effective tok/s:** 38.6  
