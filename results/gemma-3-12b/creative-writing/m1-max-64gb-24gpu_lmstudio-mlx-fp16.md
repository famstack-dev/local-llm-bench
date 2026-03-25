# Apple M1 Max / 64GB / 24 GPU cores

**Model:** mlx-community/gemma-3-12b-it-qat-fp16  
**Backend:** lmstudio-mlx-fp16  
**Scenario:** creative-writing (single-shot)  

| Turn | Context | Prefill | Gen | Gen tok/s | Effective tok/s | Total | Output |
|-----:|--------:|--------:|----:|----------:|----------------:|------:|-------:|
| 1 | 57 | 0.72s | 9.19s | 34.9 | **32.4** | 9.91s | 321 |
| 2 | 60 | 0.53s | 9.94s | 34.8 | **33.0** | 10.47s | 346 |
| 3 | 58 | 0.52s | 8.34s | 34.9 | **32.8** | 8.86s | 291 |

**Total prefill:** 1.8s  
**Total generation:** 27.5s  
**Total time:** 29.2s  
**Avg generation tok/s:** 34.9  
**Avg effective tok/s:** 32.8  
