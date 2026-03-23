# Apple M3 Max / 128GB / 40 GPU cores

**Model:** Qwen3.5-35B-A3B-4bit  
**Backend:** omlx  
**Scenario:** doc-summary (single-shot)  

| Turn | Context | Prefill | Gen | Gen tok/s | Effective tok/s | Total | Output |
|-----:|--------:|--------:|----:|----------:|----------------:|------:|-------:|
| 1 | 425 | 0.54s | 1.17s | 94.3 | **64.6** | 1.70s | 110 |
| 2 | 612 | 0.43s | 1.06s | 93.8 | **66.6** | 1.49s | 99 |
| 3 | 535 | 0.48s | 1.07s | 94.0 | **65.0** | 1.55s | 101 |
| 4 | 524 | 0.47s | 1.01s | 94.3 | **64.5** | 1.47s | 95 |
| 5 | 1,518 | 1.07s | 1.37s | 92.6 | **51.9** | 2.44s | 127 |

**Total prefill:** 3.0s  
**Total generation:** 5.7s  
**Total time:** 8.7s  
**Avg generation tok/s:** 93.8  
**Avg effective tok/s:** 61.4  
