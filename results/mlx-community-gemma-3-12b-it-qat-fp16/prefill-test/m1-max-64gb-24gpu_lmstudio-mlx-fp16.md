# Apple M1 Max / 64GB / 24 GPU cores

**Model:** mlx-community/gemma-3-12b-it-qat-fp16  
**Backend:** lmstudio-mlx-fp16  
**Scenario:** prefill-test (single-shot)  

| Turn | Context | Prefill | Gen | Gen tok/s | Effective tok/s | Total | Output |
|-----:|--------:|--------:|----:|----------:|----------------:|------:|-------:|
| 1 | 655 | 3.71s | 4.46s | 33.4 | **18.2** | 8.16s | 149 |
| 2 | 1,453 | 7.53s | 4.47s | 33.3 | **12.4** | 11.99s | 149 |
| 3 | 3,015 | 17.23s | 4.50s | 33.1 | **6.9** | 21.73s | 149 |
| 4 | 8,496 | 68.46s | 4.99s | 29.9 | **2.0** | 73.45s | 149 |

**Total prefill:** 96.9s  
**Total generation:** 18.4s  
**Total time:** 115.3s  
**Avg generation tok/s:** 32.4  
**Avg effective tok/s:** 5.2  
