# Apple M3 Max / 128GB / 40 GPU cores

**Model:** Llama-3.1-8B-Instruct  
**Backend:** omlx  
**Scenario:** creative-writing (single-shot)  

| Turn | Context | Prefill | Gen | Gen tok/s | Effective tok/s | Total | Output |
|-----:|--------:|--------:|----:|----------:|----------------:|------:|-------:|
| 1 | 57 | 0.23s | 5.90s | 76.9 | **74.0** | 6.14s | 454 |
| 2 | 60 | 0.23s | 4.32s | 76.8 | **72.9** | 4.55s | 332 |
| 3 | 58 | 0.23s | 5.21s | 76.9 | **73.6** | 5.45s | 401 |

**Total prefill:** 0.7s  
**Total generation:** 15.4s  
**Total time:** 16.1s  
**Avg generation tok/s:** 76.9  
**Avg effective tok/s:** 73.6  
