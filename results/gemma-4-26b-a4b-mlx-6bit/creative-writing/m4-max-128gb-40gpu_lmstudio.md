# Apple M4 Max / 128GB / 40 GPU cores

**Model:** gemma-4-26b-a4b-it-mlx@6bit  
**Backend:** lmstudio  
**Scenario:** creative-writing (single-shot)  

| Turn | Context | Prefill | Gen | Gen tok/s | Effective tok/s | Total | Output |
|-----:|--------:|--------:|----:|----------:|----------------:|------:|-------:|
| 1 | 57 | 0.41s | 5.09s | 85.1 | **78.8** | 5.49s | 433 |
| 2 | 60 | 0.29s | 8.03s | 84.7 | **81.7** | 8.32s | 680 |
| 3 | 58 | 0.30s | 4.03s | 86.2 | **80.2** | 4.33s | 347 |

**Total prefill:** 1.0s  
**Total generation:** 17.1s  
**Total time:** 18.1s  
**Avg generation tok/s:** 85.3  
**Avg effective tok/s:** 80.5  
