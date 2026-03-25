# Apple M1 Max / 64GB / 24 GPU cores

**Model:** Qwen3.5-35B-A3B-4bit-fp16  
**Backend:** omlx  
**Scenario:** doc-summary (single-shot)  

| Turn | Context | Prefill | Gen | Gen tok/s | Effective tok/s | Total | Output |
|-----:|--------:|--------:|----:|----------:|----------------:|------:|-------:|
| 1 | 425 | 1.35s | 1.46s | 65.9 | **34.2** | 2.81s | 96 |
| 2 | 612 | 1.17s | 1.28s | 64.9 | **33.9** | 2.44s | 83 |
| 3 | 535 | 1.28s | 1.83s | 66.8 | **39.3** | 3.11s | 122 |
| 4 | 524 | 1.24s | 1.39s | 67.6 | **35.7** | 2.63s | 94 |
| 5 | 1,518 | 2.65s | 1.83s | 64.4 | **26.3** | 4.48s | 118 |

**Total prefill:** 7.7s  
**Total generation:** 7.8s  
**Total time:** 15.5s  
**Avg generation tok/s:** 65.9  
**Avg effective tok/s:** 33.1  
