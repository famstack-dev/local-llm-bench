# Apple M3 Max / 128GB / 40 GPU cores

**Model:** Llama-3.1-8B-Instruct  
**Backend:** omlx  
**Scenario:** doc-summary (single-shot)  

| Turn | Context | Prefill | Gen | Gen tok/s | Effective tok/s | Total | Output |
|-----:|--------:|--------:|----:|----------:|----------------:|------:|-------:|
| 1 | 425 | 0.68s | 0.79s | 70.9 | **38.1** | 1.47s | 56 |
| 2 | 612 | 0.74s | 0.92s | 72.8 | **40.3** | 1.66s | 67 |
| 3 | 535 | 0.81s | 0.88s | 71.4 | **37.1** | 1.70s | 63 |
| 4 | 524 | 0.75s | 1.08s | 73.4 | **43.3** | 1.83s | 79 |
| 5 | 1,518 | 2.08s | 1.28s | 67.2 | **25.6** | 3.35s | 86 |

**Total prefill:** 5.1s  
**Total generation:** 5.0s  
**Total time:** 10.0s  
**Avg generation tok/s:** 71.1  
**Avg effective tok/s:** 35.1  
