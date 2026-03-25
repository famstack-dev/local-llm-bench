# Apple M3 Max / 128GB / 40 GPU cores

**Model:** JANGQ-AI/Qwen3.5-35B-A3B-JANG_4K  
**Backend:** omlx  
**Scenario:** prefill-test (single-shot)  

| Turn | Context | Prefill | Gen | Gen tok/s | Effective tok/s | Total | Output |
|-----:|--------:|--------:|----:|----------:|----------------:|------:|-------:|
| 1 | 655 | 2.05s | 1.66s | 62.1 | **27.8** | 3.71s | 103 |
| 2 | 1,453 | 4.49s | 2.42s | 62.1 | **21.7** | 6.90s | 150 |
| 3 | 3,015 | 10.30s | 2.55s | 58.9 | **11.7** | 12.85s | 150 |
| 4 | 8,496 | 53.28s | 3.35s | 44.8 | **2.6** | 56.63s | 150 |

**Total prefill:** 70.1s  
**Total generation:** 10.0s  
**Total time:** 80.1s  
**Avg generation tok/s:** 57.0  
**Avg effective tok/s:** 6.9  
