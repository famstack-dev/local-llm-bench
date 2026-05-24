# Apple M4 Max / 128GB / 40 GPU cores

**Model:** gemma-4-31b-it-mlx  
**Backend:** lmstudio  
**Scenario:** prefill-test (single-shot)  

| Turn | Context | Prefill | Gen | Gen tok/s | Effective tok/s | Total | Output |
|-----:|--------:|--------:|----:|----------:|----------------:|------:|-------:|
| 1 | 655 | 4.76s | 6.56s | 14.0 | **8.1** | 11.32s | 92 |
| 2 | 1,453 | 9.59s | 10.78s | 13.8 | **7.3** | 20.36s | 149 |
| 3 | 3,015 | 21.31s | 10.97s | 13.6 | **4.6** | 32.28s | 149 |
| 4 | 8,496 | 86.67s | 11.62s | 12.8 | **1.5** | 98.28s | 149 |

**Total prefill:** 122.3s  
**Total generation:** 39.9s  
**Total time:** 162.2s  
**Avg generation tok/s:** 13.6  
**Avg effective tok/s:** 3.3  
