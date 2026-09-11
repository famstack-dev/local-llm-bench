# Apple M5 Max / 48GB / 40 GPU cores

**Model:** llama3.1:8b (8.0B, Q4_K_M)  
**Backend:** ollama  
**Scenario:** prefill-test (single-shot)  

| Turn | Context | Prefill | Gen | Gen tok/s | Effective tok/s | Total | Output |
|-----:|--------:|--------:|----:|----------:|----------------:|------:|-------:|
| 1 | 655 | 0.48s | 1.06s | 86.7 | **59.7** | 1.54s | 92 |
| 2 | 1,453 | 0.94s | 1.94s | 77.5 | **52.2** | 2.87s | 150 |
| 3 | 3,015 | 2.44s | 1.97s | 76.1 | **34.0** | 4.41s | 150 |
| 4 | 8,496 | 13.13s | 2.54s | 59.0 | **9.6** | 15.67s | 150 |

**Total prefill:** 17.0s  
**Total generation:** 7.5s  
**Total time:** 24.5s  
**Avg generation tok/s:** 74.8  
**Avg effective tok/s:** 22.1  
