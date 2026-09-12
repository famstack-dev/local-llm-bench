# Apple M5 Max / 48GB / 40 GPU cores

**Model:** Qwen3.5-35B-A3B-4bit  
**Backend:** omlx  
**Scenario:** prefill-test (single-shot)  

| Turn | Context | Prefill | Gen | Gen tok/s | Effective tok/s | Total | Output |
|-----:|--------:|--------:|----:|----------:|----------------:|------:|-------:|
| 1 | 655 | 2.45s | 0.00s | 5675.6 | **0.4** | 2.45s | 1 |
| 2 | 1,453 | 1.95s | 0.00s | 6533.2 | **0.5** | 1.95s | 1 |
| 3 | 3,015 | 2.48s | 0.00s | 7989.2 | **0.4** | 2.48s | 1 |
| 4 | 8,496 | 6.59s | 0.00s | 4215.4 | **0.2** | 6.59s | 1 |

**Total prefill:** 13.5s  
**Total generation:** 0.0s  
**Total time:** 13.5s  
**Avg generation tok/s:** 6103.4  
**Avg effective tok/s:** 0.3  
