# Apple M3 Max / 128GB / 40 GPU cores

**Model:** llama-3.1-8b-instruct  
**Backend:** lmstudio  
**Scenario:** prefill-test (single-shot)  

| Turn | Context | Prefill | Gen | Gen tok/s | Effective tok/s | Total | Output |
|-----:|--------:|--------:|----:|----------:|----------------:|------:|-------:|
| 1 | 655 | 1.20s | 1.75s | 73.6 | **43.8** | 2.95s | 129 |
| 2 | 1,453 | 2.44s | 2.02s | 71.5 | **32.3** | 4.46s | 144 |
| 3 | 3,015 | 5.43s | 2.14s | 68.2 | **19.3** | 7.57s | 146 |
| 4 | 8,496 | 21.03s | 2.91s | 49.2 | **6.0** | 23.93s | 143 |

**Total prefill:** 30.1s  
**Total generation:** 8.8s  
**Total time:** 38.9s  
**Avg generation tok/s:** 65.6  
**Avg effective tok/s:** 14.4  
