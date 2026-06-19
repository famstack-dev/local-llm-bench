# Apple M4 Max / 128GB / 40 GPU cores

**Model:** gemma-4-26b-a4b-it-mlx@6bit  
**Backend:** lmstudio  
**Scenario:** prefill-test (single-shot)  

| Turn | Context | Prefill | Gen | Gen tok/s | Effective tok/s | Total | Output |
|-----:|--------:|--------:|----:|----------:|----------------:|------:|-------:|
| 1 | 655 | 0.93s | 1.02s | 86.6 | **45.2** | 1.95s | 88 |
| 2 | 1,453 | 1.53s | 1.62s | 83.9 | **43.1** | 3.15s | 136 |
| 3 | 3,015 | 3.24s | 1.85s | 80.7 | **29.3** | 5.09s | 149 |
| 4 | 8,496 | 13.18s | 2.05s | 72.6 | **9.8** | 15.23s | 149 |

**Total prefill:** 18.9s  
**Total generation:** 6.5s  
**Total time:** 25.4s  
**Avg generation tok/s:** 80.9  
**Avg effective tok/s:** 20.5  
