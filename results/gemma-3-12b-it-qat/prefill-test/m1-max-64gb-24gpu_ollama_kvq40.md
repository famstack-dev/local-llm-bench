# Apple M1 Max / 64GB / 24 GPU cores

**Model:** gemma3:12b-it-qat (12.2B, Q4_0)  
**Backend:** ollama  
**Scenario:** prefill-test (single-shot)  
**Ollama config:** kv_cache=q4_0  

| Turn | Context | Prefill | Gen | Gen tok/s | Effective tok/s | Total | Output |
|-----:|--------:|--------:|----:|----------:|----------------:|------:|-------:|
| 1 | 655 | 3.63s | 3.68s | 19.5 | **9.8** | 7.31s | 72 |
| 2 | 1,453 | 7.61s | 7.54s | 19.9 | **9.9** | 15.14s | 150 |
| 3 | 3,015 | 17.78s | 8.26s | 18.2 | **5.8** | 26.04s | 150 |
| 4 | 8,496 | 77.12s | 11.62s | 12.9 | **1.7** | 88.73s | 150 |

**Total prefill:** 106.1s  
**Total generation:** 31.1s  
**Total time:** 137.2s  
**Avg generation tok/s:** 17.6  
**Avg effective tok/s:** 3.8  
