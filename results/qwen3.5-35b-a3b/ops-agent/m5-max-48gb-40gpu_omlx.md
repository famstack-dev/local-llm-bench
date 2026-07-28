# Apple M5 Max / 48GB / 40 GPU cores

**Model:** Qwen3.5-35B-A3B-4bit  
**Backend:** omlx  
**Scenario:** ops-agent (conversation)  

| Turn | Context | Prefill | Gen | Gen tok/s | Effective tok/s | Total | Output |
|-----:|--------:|--------:|----:|----------:|----------------:|------:|-------:|
| 1 | 575 | 3.09s | 1.05s | 10.4 | **2.7** | 4.15s | 11 |
| 2 | 929 | 3.74s | 0.57s | 12.3 | **1.6** | 4.31s | 7 |
| 3 | 1,094 | 4.41s | 0.00s | 7570.9 | **0.2** | 4.41s | 1 |
| 4 | 1,861 | 2.66s | 1.24s | 9.7 | **3.1** | 3.90s | 12 |
| 5 | 2,269 | 3.43s | 1.66s | 9.7 | **3.1** | 5.09s | 16 |
| 6 | 2,690 | 2.82s | 1.47s | 9.5 | **3.3** | 4.29s | 14 |
| 7 | 2,955 | 3.27s | 1.78s | 9.6 | **3.4** | 5.05s | 17 |
| 8 | 3,337 | 3.47s | 1.54s | 9.7 | **3.0** | 5.01s | 15 |

**Total prefill:** 26.9s  
**Total generation:** 9.3s  
**Total time:** 36.2s  
**Avg generation tok/s:** 955.2  
**Avg effective tok/s:** 2.6  
