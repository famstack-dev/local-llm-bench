# Apple M1 Max / 64GB / 24 GPU cores

**Model:** mlx-community/gemma-3-12b-it-qat-fp16  
**Backend:** lmstudio-mlx-fp16-chunked  
**Scenario:** prefill-test (single-shot)  

| Turn | Context | Prefill | Gen | Gen tok/s | Effective tok/s | Total | Output |
|-----:|--------:|--------:|----:|----------:|----------------:|------:|-------:|
| 1 | 655 | 3.71s | 4.52s | 32.9 | **18.1** | 8.23s | 149 |
| 2 | 1,453 | 7.53s | 4.50s | 33.1 | **12.4** | 12.03s | 149 |
| 3 | 3,015 | 18.16s | 4.59s | 32.4 | **6.5** | 22.76s | 149 |
| 4 | 8,496 | 72.67s | 5.32s | 28.0 | **1.9** | 77.99s | 149 |

**Total prefill:** 102.1s  
**Total generation:** 18.9s  
**Total time:** 121.0s  
**Avg generation tok/s:** 31.6  
**Avg effective tok/s:** 4.9  
