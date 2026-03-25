# Apple M3 Max / 128GB / 40 GPU cores

**Model:** JANGQ-AI/Qwen3.5-35B-A3B-JANG_4K  
**Backend:** omlx  
**Scenario:** creative-writing (single-shot)  

| Turn | Context | Prefill | Gen | Gen tok/s | Effective tok/s | Total | Output |
|-----:|--------:|--------:|----:|----------:|----------------:|------:|-------:|
| 1 | 57 | 0.25s | 6.54s | 64.0 | **61.6** | 6.80s | 419 |
| 2 | 60 | 0.24s | 9.16s | 63.8 | **62.2** | 9.41s | 585 |
| 3 | 58 | 0.25s | 6.61s | 63.8 | **61.6** | 6.86s | 422 |

**Total prefill:** 0.7s  
**Total generation:** 22.3s  
**Total time:** 23.1s  
**Avg generation tok/s:** 63.9  
**Avg effective tok/s:** 61.8  
