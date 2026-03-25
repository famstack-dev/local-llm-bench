# Apple M3 Max / 128GB / 40 GPU cores

**Model:** Qwen3.5-35B-A3B-4bit  
**Backend:** omlx  
**Scenario:** ops-agent (conversation)  

| Turn | Context | Prefill | Gen | Gen tok/s | Effective tok/s | Total | Output |
|-----:|--------:|--------:|----:|----------:|----------------:|------:|-------:|
| 1 | 575 | 0.61s | 3.02s | 92.8 | **77.2** | 3.63s | 280 |
| 2 | 1,079 | 1.05s | 3.83s | 92.2 | **72.4** | 4.87s | 353 |
| 3 | 1,535 | 1.43s | 3.02s | 91.5 | **62.1** | 4.45s | 276 |
| 4 | 2,030 | 0.56s | 4.10s | 91.2 | **80.3** | 4.66s | 374 |
| 5 | 2,672 | 1.00s | 3.57s | 90.8 | **70.8** | 4.58s | 324 |
| 6 | 3,229 | 1.61s | 3.28s | 89.6 | **60.1** | 4.89s | 294 |
| 7 | 3,607 | 0.54s | 3.69s | 89.3 | **78.0** | 4.22s | 329 |
| 8 | 4,124 | 0.94s | 3.82s | 89.0 | **71.4** | 4.76s | 340 |

**Total prefill:** 7.7s  
**Total generation:** 28.3s  
**Total time:** 36.1s  
**Avg generation tok/s:** 90.8  
**Avg effective tok/s:** 71.3  
