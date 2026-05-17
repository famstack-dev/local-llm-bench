# Apple M4 Max / 128GB / 40 GPU cores

**Model:** qwen3.6-35b-a3b  
**Backend:** lmstudio-mlx  
**Scenario:** prefill-test (single-shot)  

| Turn | Context | Prefill | Gen | Gen tok/s | Effective tok/s | Total | Output |
|-----:|--------:|--------:|----:|----------:|----------------:|------:|-------:|
| 1 | 655 | 0.76s | 1.20s | 88.1 | **54.1** | 1.96s | 106 |
| 2 | 1,453 | 1.25s | 1.67s | 85.0 | **48.6** | 2.92s | 142 |
| 3 | 3,015 | 2.54s | 1.44s | 86.4 | **31.2** | 3.97s | 124 |
| 4 | 8,496 | 10.82s | 1.32s | 82.6 | **9.0** | 12.14s | 109 |

**Total prefill:** 15.4s  
**Total generation:** 5.6s  
**Total time:** 21.0s  
**Avg generation tok/s:** 85.5  
**Avg effective tok/s:** 22.9  
