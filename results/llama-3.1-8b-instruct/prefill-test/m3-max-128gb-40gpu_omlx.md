# Apple M3 Max / 128GB / 40 GPU cores

**Model:** Llama-3.1-8B-Instruct  
**Backend:** omlx  
**Scenario:** prefill-test (single-shot)  

| Turn | Context | Prefill | Gen | Gen tok/s | Effective tok/s | Total | Output |
|-----:|--------:|--------:|----:|----------:|----------------:|------:|-------:|
| 1 | 655 | 1.28s | 2.04s | 72.1 | **44.3** | 3.32s | 147 |
| 2 | 1,453 | 2.69s | 2.12s | 69.2 | **30.5** | 4.82s | 147 |
| 3 | 3,015 | 5.72s | 2.26s | 66.3 | **18.8** | 7.98s | 150 |
| 4 | 8,496 | 21.32s | 3.26s | 45.1 | **6.0** | 24.58s | 147 |

**Total prefill:** 31.0s  
**Total generation:** 9.7s  
**Total time:** 40.7s  
**Avg generation tok/s:** 63.2  
**Avg effective tok/s:** 14.5  
