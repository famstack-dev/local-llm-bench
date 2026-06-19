# Apple M4 Max / 128GB / 40 GPU cores

**Model:** qwen/qwen3-coder-next  
**Backend:** lmstudio  
**Scenario:** doc-summary (single-shot)  

| Turn | Context | Prefill | Gen | Gen tok/s | Effective tok/s | Total | Output |
|-----:|--------:|--------:|----:|----------:|----------------:|------:|-------:|
| 1 | 425 | 1.35s | 1.82s | 70.8 | **40.7** | 3.17s | 129 |
| 2 | 612 | 0.64s | 1.37s | 70.0 | **47.9** | 2.01s | 96 |
| 3 | 535 | 0.69s | 1.65s | 69.9 | **49.3** | 2.33s | 115 |
| 4 | 524 | 0.66s | 1.88s | 70.4 | **52.0** | 2.54s | 132 |
| 5 | 1,518 | 1.36s | 2.10s | 68.5 | **41.5** | 3.47s | 144 |

**Total prefill:** 4.7s  
**Total generation:** 8.8s  
**Total time:** 13.5s  
**Avg generation tok/s:** 69.9  
**Avg effective tok/s:** 45.6  
