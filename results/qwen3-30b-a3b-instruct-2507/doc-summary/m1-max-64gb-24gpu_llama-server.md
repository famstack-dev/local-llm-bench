# Apple M1 Max / 64GB / 24 GPU cores

**Model:** Qwen3-30B-A3B-Instruct-2507  
**Backend:** llama-server  
**Scenario:** doc-summary (single-shot)  

| Turn | Context | Prefill | Gen | Gen tok/s | Effective tok/s | Total | Output |
|-----:|--------:|--------:|----:|----------:|----------------:|------:|-------:|
| 1 | 425 | 1.06s | 2.10s | 55.7 | **37.1** | 3.16s | 117 |
| 2 | 612 | 0.72s | 1.92s | 55.3 | **40.1** | 2.64s | 106 |
| 3 | 535 | 0.82s | 1.91s | 56.0 | **39.2** | 2.73s | 107 |
| 4 | 524 | 0.79s | 1.89s | 55.6 | **39.2** | 2.68s | 105 |
| 5 | 1,518 | 2.95s | 2.96s | 50.6 | **25.4** | 5.91s | 150 |

**Total prefill:** 6.3s  
**Total generation:** 10.8s  
**Total time:** 17.1s  
**Avg generation tok/s:** 54.6  
**Avg effective tok/s:** 34.2  
