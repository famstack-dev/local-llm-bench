# Apple M4 Max / 128GB / 40 GPU cores

**Model:** gemma-4-e4b-it-mlx  
**Backend:** lmstudio  
**Scenario:** ops-agent (conversation)  

| Turn | Context | Prefill | Gen | Gen tok/s | Effective tok/s | Total | Output |
|-----:|--------:|--------:|----:|----------:|----------------:|------:|-------:|
| 1 | 575 | 0.63s | 3.90s | 72.1 | **62.1** | 4.53s | 281 |
| 2 | 1,063 | 0.40s | 2.98s | 71.4 | **63.0** | 3.38s | 213 |
| 3 | 1,398 | 0.28s | 3.13s | 71.0 | **65.1** | 3.41s | 222 |
| 4 | 1,847 | 0.37s | 3.11s | 71.0 | **63.5** | 3.48s | 221 |
| 5 | 2,322 | 0.38s | 3.43s | 70.6 | **63.6** | 3.81s | 242 |
| 6 | 2,818 | 0.43s | 1.84s | 71.2 | **57.7** | 2.27s | 131 |
| 7 | 3,045 | 0.28s | 2.71s | 70.0 | **63.4** | 3.00s | 190 |
| 8 | 3,422 | 0.34s | 3.56s | 69.6 | **63.5** | 3.90s | 248 |

**Total prefill:** 3.1s  
**Total generation:** 24.7s  
**Total time:** 27.8s  
**Avg generation tok/s:** 70.9  
**Avg effective tok/s:** 62.9  
