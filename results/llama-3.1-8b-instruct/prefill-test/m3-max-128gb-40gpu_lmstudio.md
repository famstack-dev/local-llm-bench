# Apple M3 Max / 128GB / 40 GPU cores

**Model:** llama-3.1-8b-instruct  
**Backend:** lmstudio  
**Scenario:** prefill-test (single-shot)  

| Turn | Context | Prefill | Gen | Gen tok/s | Effective tok/s | Total | Output |
|-----:|--------:|--------:|----:|----------:|----------------:|------:|-------:|
| 1 | 655 | 1.13s | 6.20s | 23.7 | **20.0** | 7.33s | 147 |
| 2 | 1,453 | 2.15s | 6.21s | 22.7 | **16.8** | 8.37s | 141 |
| 3 | 3,015 | 4.58s | 6.39s | 22.8 | **13.3** | 10.97s | 146 |
| 4 | 8,496 | 18.01s | 6.95s | 20.7 | **5.8** | 24.96s | 144 |

**Total prefill:** 25.9s  
**Total generation:** 25.8s  
**Total time:** 51.6s  
**Avg generation tok/s:** 22.5  
**Avg effective tok/s:** 11.2  
