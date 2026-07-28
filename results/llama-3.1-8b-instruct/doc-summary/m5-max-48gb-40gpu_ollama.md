# Apple M5 Max / 48GB / 40 GPU cores

**Model:** llama3.1:8b (8.0B, Q4_K_M)  
**Backend:** ollama  
**Scenario:** doc-summary (single-shot)  

| Turn | Context | Prefill | Gen | Gen tok/s | Effective tok/s | Total | Output |
|-----:|--------:|--------:|----:|----------:|----------------:|------:|-------:|
| 1 | 425 | 0.32s | 0.84s | 88.3 | **64.1** | 1.15s | 74 |
| 2 | 612 | 0.28s | 0.82s | 87.7 | **65.5** | 1.10s | 72 |
| 3 | 535 | 0.29s | 0.67s | 80.4 | **56.1** | 0.96s | 54 |
| 4 | 524 | 0.29s | 0.70s | 79.8 | **56.3** | 0.99s | 56 |
| 5 | 1,518 | 0.84s | 1.05s | 77.2 | **42.9** | 1.89s | 81 |

**Total prefill:** 2.0s  
**Total generation:** 4.1s  
**Total time:** 6.1s  
**Avg generation tok/s:** 82.7  
**Avg effective tok/s:** 55.2  
