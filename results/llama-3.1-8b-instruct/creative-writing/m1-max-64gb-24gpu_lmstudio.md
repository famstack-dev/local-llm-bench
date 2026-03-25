# Apple M1 Max / 64GB / 24 GPU cores

**Model:** mlx-community/meta-llama-3.1-8B-instruct  
**Backend:** lmstudio  
**Scenario:** creative-writing (single-shot)  

| Turn | Context | Prefill | Gen | Gen tok/s | Effective tok/s | Total | Output |
|-----:|--------:|--------:|----:|----------:|----------------:|------:|-------:|
| 1 | 57 | 0.49s | 6.79s | 61.7 | **57.5** | 7.28s | 419 |
| 2 | 60 | 0.30s | 6.84s | 61.9 | **59.2** | 7.14s | 423 |
| 3 | 58 | 0.28s | 6.49s | 62.6 | **60.0** | 6.77s | 406 |

**Total prefill:** 1.1s  
**Total generation:** 20.1s  
**Total time:** 21.2s  
**Avg generation tok/s:** 62.1  
**Avg effective tok/s:** 58.9  
