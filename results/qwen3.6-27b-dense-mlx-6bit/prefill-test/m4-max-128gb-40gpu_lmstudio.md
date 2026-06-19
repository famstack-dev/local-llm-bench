# Apple M4 Max / 128GB / 40 GPU cores

**Model:** qwen3.6-27b  
**Backend:** lmstudio  
**Scenario:** prefill-test (single-shot)  

| Turn | Context | Prefill | Gen | Gen tok/s | Effective tok/s | Total | Output |
|-----:|--------:|--------:|----:|----------:|----------------:|------:|-------:|
| 1 | 655 | 3.94s | 3.73s | 21.7 | **10.6** | 7.67s | 81 |
| 2 | 1,453 | 7.98s | 7.01s | 20.4 | **9.5** | 14.99s | 143 |
| 3 | 3,015 | 16.57s | 5.52s | 20.1 | **5.0** | 22.10s | 111 |
| 4 | 8,496 | 67.00s | 7.53s | 19.3 | **1.9** | 74.52s | 145 |

**Total prefill:** 95.5s  
**Total generation:** 23.8s  
**Total time:** 119.3s  
**Avg generation tok/s:** 20.4  
**Avg effective tok/s:** 4.0  
