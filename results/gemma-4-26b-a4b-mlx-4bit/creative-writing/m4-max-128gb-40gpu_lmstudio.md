# Apple M4 Max / 128GB / 40 GPU cores

**Model:** gemma-4-26b-a4b-it-mlx@4bit  
**Backend:** lmstudio  
**Scenario:** creative-writing (single-shot)  

| Turn | Context | Prefill | Gen | Gen tok/s | Effective tok/s | Total | Output |
|-----:|--------:|--------:|----:|----------:|----------------:|------:|-------:|
| 1 | 57 | 0.36s | 3.67s | 106.5 | **97.1** | 4.03s | 391 |
| 2 | 60 | 0.26s | 7.64s | 105.1 | **101.7** | 7.90s | 803 |
| 3 | 58 | 0.25s | 3.45s | 106.4 | **99.2** | 3.70s | 367 |

**Total prefill:** 0.9s  
**Total generation:** 14.8s  
**Total time:** 15.6s  
**Avg generation tok/s:** 106.0  
**Avg effective tok/s:** 99.9  
