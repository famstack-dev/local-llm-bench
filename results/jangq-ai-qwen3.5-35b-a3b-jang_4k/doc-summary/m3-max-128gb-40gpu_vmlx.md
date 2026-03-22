# Apple M3 Max / 128GB / 40 GPU cores

**Model:** JANGQ-AI/Qwen3.5-35B-A3B-JANG_4K  
**Backend:** omlx  
**Scenario:** doc-summary (single-shot)  

| Turn | Context | Prefill | Gen | Gen tok/s | Effective tok/s | Total | Output |
|-----:|--------:|--------:|----:|----------:|----------------:|------:|-------:|
| 1 | 425 | 1.34s | 1.53s | 62.6 | **33.4** | 2.88s | 96 |
| 2 | 612 | 1.24s | 1.37s | 62.9 | **33.0** | 2.61s | 86 |
| 3 | 535 | 1.43s | 1.35s | 62.4 | **30.3** | 2.77s | 84 |
| 4 | 524 | 1.37s | 2.11s | 62.9 | **38.2** | 3.48s | 133 |
| 5 | 1,518 | 3.66s | 1.77s | 61.7 | **20.1** | 5.42s | 109 |

**Total prefill:** 9.0s  
**Total generation:** 8.1s  
**Total time:** 17.2s  
**Avg generation tok/s:** 62.5  
**Avg effective tok/s:** 29.6  
