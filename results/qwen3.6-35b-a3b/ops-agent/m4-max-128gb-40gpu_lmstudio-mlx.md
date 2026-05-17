# Apple M4 Max / 128GB / 40 GPU cores

**Model:** qwen3.6-35b-a3b  
**Backend:** lmstudio-mlx  
**Scenario:** ops-agent (conversation)  

| Turn | Context | Prefill | Gen | Gen tok/s | Effective tok/s | Total | Output |
|-----:|--------:|--------:|----:|----------:|----------------:|------:|-------:|
| 1 | 575 | 0.79s | 2.20s | 87.7 | **64.5** | 2.99s | 193 |
| 2 | 1,007 | 0.64s | 3.61s | 85.6 | **72.8** | 4.24s | 309 |
| 3 | 1,402 | 0.56s | 2.32s | 86.6 | **69.9** | 2.88s | 201 |
| 4 | 1,827 | 0.58s | 4.18s | 85.6 | **75.1** | 4.76s | 358 |
| 5 | 2,471 | 0.70s | 4.28s | 84.1 | **72.3** | 4.98s | 360 |
| 6 | 3,066 | 0.78s | 2.01s | 85.4 | **61.7** | 2.79s | 172 |
| 7 | 3,327 | 0.47s | 4.45s | 85.1 | **76.9** | 4.93s | 379 |
| 8 | 3,917 | 0.69s | 3.60s | 84.1 | **70.5** | 4.30s | 303 |

**Total prefill:** 5.2s  
**Total generation:** 26.7s  
**Total time:** 31.9s  
**Avg generation tok/s:** 85.5  
**Avg effective tok/s:** 71.4  
