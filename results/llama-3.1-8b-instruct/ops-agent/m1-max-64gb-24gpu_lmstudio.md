# Apple M1 Max / 64GB / 24 GPU cores

**Model:** mlx-community/meta-llama-3.1-8B-instruct  
**Backend:** lmstudio  
**Scenario:** ops-agent (conversation)  

| Turn | Context | Prefill | Gen | Gen tok/s | Effective tok/s | Total | Output |
|-----:|--------:|--------:|----:|----------:|----------------:|------:|-------:|
| 1 | 575 | 2.19s | 3.31s | 57.4 | **34.6** | 5.50s | 190 |
| 2 | 1,003 | 1.18s | 3.42s | 58.7 | **43.6** | 4.61s | 201 |
| 3 | 1,356 | 0.62s | 3.66s | 56.8 | **48.6** | 4.28s | 208 |
| 4 | 1,816 | 0.98s | 2.73s | 55.7 | **41.0** | 3.71s | 152 |
| 5 | 2,242 | 1.43s | 4.67s | 53.5 | **41.0** | 6.10s | 250 |
| 6 | 2,752 | 1.31s | 2.70s | 54.1 | **36.4** | 4.01s | 146 |
| 7 | 3,055 | 0.57s | 2.92s | 52.7 | **44.1** | 3.49s | 154 |
| 8 | 3,431 | 1.05s | 2.99s | 51.4 | **38.1** | 4.05s | 154 |

**Total prefill:** 9.3s  
**Total generation:** 26.4s  
**Total time:** 35.7s  
**Avg generation tok/s:** 55.0  
**Avg effective tok/s:** 40.7  
