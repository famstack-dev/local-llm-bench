# Apple M4 Max / 128GB / 40 GPU cores

**Model:** gemma-4-31b-it-mlx  
**Backend:** lmstudio  
**Scenario:** ops-agent (conversation)  

| Turn | Context | Prefill | Gen | Gen tok/s | Effective tok/s | Total | Output |
|-----:|--------:|--------:|----:|----------:|----------------:|------:|-------:|
| 1 | 575 | 4.77s | 7.73s | 14.0 | **8.6** | 12.50s | 108 |
| 2 | 923 | 3.87s | 10.06s | 13.9 | **10.1** | 13.93s | 140 |
| 3 | 1,157 | 2.44s | 8.80s | 13.9 | **10.9** | 11.24s | 122 |
| 4 | 1,490 | 3.25s | 9.36s | 13.6 | **10.1** | 12.60s | 127 |
| 5 | 1,861 | 3.50s | 13.95s | 13.6 | **10.8** | 17.45s | 189 |
| 6 | 2,288 | 4.22s | 9.70s | 13.7 | **9.5** | 13.93s | 133 |
| 7 | 2,512 | 2.20s | 9.57s | 13.5 | **11.0** | 11.77s | 129 |
| 8 | 2,833 | 3.07s | 13.13s | 13.5 | **10.9** | 16.21s | 177 |

**Total prefill:** 27.3s  
**Total generation:** 82.3s  
**Total time:** 109.6s  
**Avg generation tok/s:** 13.7  
**Avg effective tok/s:** 10.3  
