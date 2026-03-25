# Apple M1 Max / 64GB / 24 GPU cores

**Model:** mlx-community/gemma-3-12b-it-qat-fp16  
**Backend:** lmstudio-mlx-fp16  
**Scenario:** doc-summary (single-shot)  

| Turn | Context | Prefill | Gen | Gen tok/s | Effective tok/s | Total | Output |
|-----:|--------:|--------:|----:|----------:|----------------:|------:|-------:|
| 1 | 425 | 2.66s | 3.12s | 34.6 | **18.7** | 5.78s | 108 |
| 2 | 612 | 2.17s | 2.51s | 35.1 | **18.8** | 4.68s | 88 |
| 3 | 535 | 2.41s | 2.39s | 34.7 | **17.3** | 4.81s | 83 |
| 4 | 524 | 2.39s | 2.79s | 34.4 | **18.5** | 5.18s | 96 |
| 5 | 1,518 | 6.43s | 3.25s | 33.9 | **11.4** | 9.68s | 110 |

**Total prefill:** 16.1s  
**Total generation:** 14.1s  
**Total time:** 30.1s  
**Avg generation tok/s:** 34.5  
**Avg effective tok/s:** 16.1  
