# Apple M1 Max / 64GB / 24 GPU cores

**Model:** Qwen3.5-35B-A3B-4bit  
**Backend:** omlx  
**Scenario:** prefill-test (single-shot)  

| Turn | Context | Prefill | Gen | Gen tok/s | Effective tok/s | Total | Output |
|-----:|--------:|--------:|----:|----------:|----------------:|------:|-------:|
| 1 | 655 | 2.12s | 1.90s | 54.8 | **25.9** | 4.02s | 104 |
| 2 | 1,453 | 2.06s | 2.62s | 55.0 | **30.8** | 4.68s | 144 |
| 3 | 3,015 | 2.38s | 2.11s | 52.6 | **24.7** | 4.49s | 111 |
| 4 | 8,496 | 1.73s | 3.12s | 45.8 | **29.5** | 4.86s | 143 |

**Total prefill:** 8.3s  
**Total generation:** 9.7s  
**Total time:** 18.0s  
**Avg generation tok/s:** 52.0  
**Avg effective tok/s:** 27.8  
