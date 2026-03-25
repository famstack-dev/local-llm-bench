# Apple M2 Pro / 32GB / 19 GPU cores

**Model:** GLM-4.7-Flash-4bit  
**Backend:** omlx  
**Scenario:** prefill-test (single-shot)  

| Turn | Context | Prefill | Gen | Gen tok/s | Effective tok/s | Total | Output |
|-----:|--------:|--------:|----:|----------:|----------------:|------:|-------:|
| 1 | 655 | 2.91s | 3.12s | 40.4 | **20.9** | 6.03s | 126 |
| 2 | 1,453 | 6.07s | 3.84s | 38.3 | **14.8** | 9.91s | 147 |
| 3 | 3,015 | 14.04s | 4.26s | 35.2 | **8.2** | 18.30s | 150 |
| 4 | 8,496 | 68.66s | 6.38s | 23.5 | **2.0** | 75.05s | 150 |

**Total prefill:** 91.7s  
**Total generation:** 17.6s  
**Total time:** 109.3s  
**Avg generation tok/s:** 34.3  
**Avg effective tok/s:** 5.2  
