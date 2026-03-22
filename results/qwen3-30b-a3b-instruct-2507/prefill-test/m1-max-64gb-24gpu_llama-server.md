# Apple M1 Max / 64GB / 24 GPU cores

**Model:** Qwen3-30B-A3B-Instruct-2507  
**Backend:** llama-server  
**Scenario:** prefill-test (single-shot)  

| Turn | Context | Prefill | Gen | Gen tok/s | Effective tok/s | Total | Output |
|-----:|--------:|--------:|----:|----------:|----------------:|------:|-------:|
| 1 | 655 | 1.42s | 2.93s | 51.2 | **34.5** | 4.35s | 150 |
| 2 | 1,453 | 3.20s | 3.02s | 49.7 | **24.1** | 6.21s | 150 |
| 3 | 3,015 | 7.51s | 3.38s | 44.4 | **13.8** | 10.89s | 150 |
| 4 | 8,496 | 48.58s | 4.61s | 31.7 | **2.7** | 53.19s | 146 |

**Total prefill:** 60.7s  
**Total generation:** 13.9s  
**Total time:** 74.6s  
**Avg generation tok/s:** 44.2  
**Avg effective tok/s:** 8.0  
