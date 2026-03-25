# Apple M1 Max / 64GB / 24 GPU cores

**Model:** llama3.1:8b (8.0B, Q4_K_M)  
**Backend:** ollama  
**Scenario:** prefill-test (single-shot)  

| Turn | Context | Prefill | Gen | Gen tok/s | Effective tok/s | Total | Output |
|-----:|--------:|--------:|----:|----------:|----------------:|------:|-------:|
| 1 | 655 | 2.23s | 2.77s | 37.5 | **20.8** | 5.01s | 104 |
| 2 | 1,453 | 4.59s | 4.29s | 35.0 | **16.9** | 8.88s | 150 |
| 3 | 3,015 | 11.28s | 4.93s | 30.4 | **9.3** | 16.21s | 150 |
| 4 | 8,496 | 58.01s | 7.55s | 19.9 | **2.3** | 65.56s | 150 |

**Total prefill:** 76.1s  
**Total generation:** 19.5s  
**Total time:** 95.7s  
**Avg generation tok/s:** 30.7  
**Avg effective tok/s:** 5.8  
