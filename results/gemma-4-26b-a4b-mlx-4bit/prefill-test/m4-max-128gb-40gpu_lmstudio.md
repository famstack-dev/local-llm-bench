# Apple M4 Max / 128GB / 40 GPU cores

**Model:** gemma-4-26b-a4b-it-mlx@4bit  
**Backend:** lmstudio  
**Scenario:** prefill-test (single-shot)  

| Turn | Context | Prefill | Gen | Gen tok/s | Effective tok/s | Total | Output |
|-----:|--------:|--------:|----:|----------:|----------------:|------:|-------:|
| 1 | 655 | 0.87s | 0.84s | 108.5 | **53.2** | 1.71s | 91 |
| 2 | 1,453 | 1.42s | 1.32s | 102.1 | **49.3** | 2.74s | 135 |
| 3 | 3,015 | 3.08s | 1.55s | 96.1 | **32.2** | 4.63s | 149 |
| 4 | 8,496 | 18.53s | 1.66s | 89.9 | **7.4** | 20.19s | 149 |

**Total prefill:** 23.9s  
**Total generation:** 5.4s  
**Total time:** 29.3s  
**Avg generation tok/s:** 99.2  
**Avg effective tok/s:** 17.9  
