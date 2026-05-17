# Apple M4 Max / 128GB / 40 GPU cores

**Model:** qwen/qwen3-coder-next  
**Backend:** lmstudio  
**Scenario:** ops-agent (conversation)  

| Turn | Context | Prefill | Gen | Gen tok/s | Effective tok/s | Total | Output |
|-----:|--------:|--------:|----:|----------:|----------------:|------:|-------:|
| 1 | 575 | 1.53s | 4.04s | 67.2 | **48.7** | 5.57s | 271 |
| 2 | 1,043 | 0.67s | 2.74s | 70.5 | **56.7** | 3.40s | 193 |
| 3 | 1,341 | 0.48s | 2.23s | 69.5 | **57.1** | 2.71s | 155 |
| 4 | 1,700 | 0.55s | 2.41s | 68.4 | **55.7** | 2.96s | 165 |
| 5 | 2,102 | 0.54s | 4.14s | 66.7 | **59.0** | 4.68s | 276 |
| 6 | 2,596 | 0.64s | 3.26s | 66.9 | **56.0** | 3.89s | 218 |
| 7 | 2,889 | 0.46s | 2.94s | 67.6 | **58.5** | 3.40s | 199 |
| 8 | 3,274 | 0.75s | 4.85s | 66.2 | **57.4** | 5.60s | 321 |

**Total prefill:** 5.6s  
**Total generation:** 26.6s  
**Total time:** 32.2s  
**Avg generation tok/s:** 67.9  
**Avg effective tok/s:** 55.8  
