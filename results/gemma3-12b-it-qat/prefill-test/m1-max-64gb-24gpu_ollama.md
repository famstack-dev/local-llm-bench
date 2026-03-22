# Apple M1 Max / 64GB / 24 GPU cores

**Model:** gemma3:12b-it-qat (12.2B, Q4_0)  
**Backend:** ollama  
**Scenario:** prefill-test (single-shot)  

| Turn | Context | Prefill | Gen | Gen tok/s | Effective tok/s | Total | Output |
|-----:|--------:|--------:|----:|----------:|----------------:|------:|-------:|
| 1 | 655 | 3.59s | 3.90s | 18.7 | **9.8** | 7.49s | 73 |
| 2 | 1,453 | 7.62s | 7.70s | 19.5 | **9.8** | 15.32s | 150 |
| 3 | 3,015 | 18.35s | 8.56s | 17.5 | **5.6** | 26.92s | 150 |
| 4 | 8,496 | 79.27s | 12.13s | 12.4 | **1.6** | 91.39s | 150 |

**Total prefill:** 108.8s  
**Total generation:** 32.3s  
**Total time:** 141.1s  
**Avg generation tok/s:** 17.0  
**Avg effective tok/s:** 3.7  
