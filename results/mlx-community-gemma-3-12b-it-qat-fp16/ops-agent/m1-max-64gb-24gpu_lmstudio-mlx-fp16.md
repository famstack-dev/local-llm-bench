# Apple M1 Max / 64GB / 24 GPU cores

**Model:** mlx-community/gemma-3-12b-it-qat-fp16  
**Backend:** lmstudio-mlx-fp16  
**Scenario:** ops-agent (conversation)  

| Turn | Context | Prefill | Gen | Gen tok/s | Effective tok/s | Total | Output |
|-----:|--------:|--------:|----:|----------:|----------------:|------:|-------:|
| 1 | 575 | 3.71s | 1.89s | 34.9 | **11.8** | 5.60s | 66 |
| 2 | 876 | 2.49s | 5.90s | 33.6 | **23.6** | 8.39s | 198 |
| 3 | 1,186 | 1.28s | 4.58s | 33.6 | **26.3** | 5.86s | 154 |
| 4 | 1,558 | 2.02s | 1.43s | 35.8 | **14.8** | 3.45s | 51 |
| 5 | 1,854 | 2.10s | 4.37s | 33.0 | **22.3** | 6.47s | 144 |
| 6 | 2,238 | 2.40s | 1.50s | 34.6 | **13.3** | 3.90s | 52 |
| 7 | 2,405 | 1.12s | 1.97s | 33.5 | **21.4** | 3.09s | 66 |
| 8 | 2,652 | 1.77s | 2.89s | 33.3 | **20.6** | 4.66s | 96 |

**Total prefill:** 16.9s  
**Total generation:** 24.5s  
**Total time:** 41.4s  
**Avg generation tok/s:** 34.0  
**Avg effective tok/s:** 20.0  
