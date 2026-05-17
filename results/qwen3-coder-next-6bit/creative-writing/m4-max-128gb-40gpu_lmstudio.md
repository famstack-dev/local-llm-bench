# Apple M4 Max / 128GB / 40 GPU cores

**Model:** qwen/qwen3-coder-next  
**Backend:** lmstudio  
**Scenario:** creative-writing (single-shot)  

| Turn | Context | Prefill | Gen | Gen tok/s | Effective tok/s | Total | Output |
|-----:|--------:|--------:|----:|----------:|----------------:|------:|-------:|
| 1 | 57 | 0.33s | 8.70s | 70.7 | **68.1** | 9.03s | 615 |
| 2 | 60 | 0.30s | 8.69s | 69.5 | **67.2** | 8.98s | 604 |
| 3 | 58 | 0.33s | 9.09s | 70.4 | **67.9** | 9.42s | 640 |

**Total prefill:** 1.0s  
**Total generation:** 26.5s  
**Total time:** 27.4s  
**Avg generation tok/s:** 70.2  
**Avg effective tok/s:** 67.8  
