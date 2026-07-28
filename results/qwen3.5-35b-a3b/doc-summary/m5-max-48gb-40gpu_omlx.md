# Apple M5 Max / 48GB / 40 GPU cores

**Model:** Qwen3.5-35B-A3B-4bit  
**Backend:** omlx  
**Scenario:** doc-summary (single-shot)  

| Turn | Context | Prefill | Gen | Gen tok/s | Effective tok/s | Total | Output |
|-----:|--------:|--------:|----:|----------:|----------------:|------:|-------:|
| 1 | 425 | 1.49s | 0.00s | 8943.1 | **0.7** | 1.49s | 1 |
| 2 | 612 | 1.45s | 0.00s | 4382.8 | **0.7** | 1.45s | 1 |
| 3 | 535 | 1.51s | 0.00s | 4739.3 | **0.7** | 1.51s | 1 |
| 4 | 524 | 1.46s | 0.00s | 4609.1 | **0.7** | 1.46s | 1 |
| 5 | 1,518 | 1.69s | 0.00s | 5882.6 | **0.6** | 1.69s | 1 |

**Total prefill:** 7.6s  
**Total generation:** 0.0s  
**Total time:** 7.6s  
**Avg generation tok/s:** 5711.4  
**Avg effective tok/s:** 0.7  
