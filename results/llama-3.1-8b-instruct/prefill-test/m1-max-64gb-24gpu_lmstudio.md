# Apple M1 Max / 64GB / 24 GPU cores

**Model:** mlx-community/meta-llama-3.1-8B-instruct  
**Backend:** lmstudio  
**Scenario:** prefill-test (single-shot)  

| Turn | Context | Prefill | Gen | Gen tok/s | Effective tok/s | Total | Output |
|-----:|--------:|--------:|----:|----------:|----------------:|------:|-------:|
| 1 | 655 | 2.12s | 2.46s | 59.7 | **32.1** | 4.58s | 147 |
| 2 | 1,453 | 4.28s | 2.54s | 57.0 | **21.3** | 6.82s | 145 |
| 3 | 3,015 | 9.74s | 2.77s | 52.7 | **11.7** | 12.51s | 146 |
| 4 | 8,496 | 41.33s | 3.79s | 37.7 | **3.2** | 45.12s | 143 |

**Total prefill:** 57.5s  
**Total generation:** 11.6s  
**Total time:** 69.0s  
**Avg generation tok/s:** 51.8  
**Avg effective tok/s:** 8.4  
