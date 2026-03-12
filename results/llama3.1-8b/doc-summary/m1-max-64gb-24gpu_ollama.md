# Apple M1 Max / 64GB / 24 GPU cores

**Model:** llama3.1:8b (8.0B, Q4_K_M)  
**Backend:** ollama  
**Scenario:** doc-summary (single-shot)  

| Turn | Context | Prefill | Gen | Tok/s | Total | Output |
|-----:|--------:|--------:|----:|------:|------:|-------:|
| 1 | 425 | 1.49s | 1.61s | 37.2 | 3.10s | 60 |
| 2 | 612 | 1.24s | 1.52s | 37.5 | 2.76s | 57 |
| 3 | 535 | 1.42s | 1.64s | 37.3 | 3.06s | 61 |
| 4 | 524 | 1.24s | 1.58s | 37.4 | 2.81s | 59 |
| 5 | 1,518 | 4.23s | 2.17s | 35.1 | 6.39s | 76 |

**Total prefill:** 9.6s  
**Total generation:** 8.5s  
**Total time:** 18.1s  
**Avg generation tok/s:** 36.9  
