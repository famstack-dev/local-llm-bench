# Apple M1 Max / 64GB / 24 GPU cores

**Model:** qwen3-30b-a3b-instruct-2507  
**Backend:** lmstudio-gguf  
**Scenario:** prefill-test (single-shot)  

| Turn | Context | Prefill | Gen | Gen tok/s | Effective tok/s | Total | Output |
|-----:|--------:|--------:|----:|----------:|----------------:|------:|-------:|
| 1 | 655 | 1.57s | 2.28s | 54.8 | **32.4** | 3.85s | 125 |
| 2 | 1,453 | 3.29s | 2.90s | 51.1 | **23.9** | 6.18s | 148 |
| 3 | 3,015 | 7.68s | 3.08s | 48.0 | **13.7** | 10.77s | 148 |
| 4 | 8,496 | 49.12s | 4.38s | 33.3 | **2.7** | 53.49s | 146 |

**Total prefill:** 61.7s  
**Total generation:** 12.6s  
**Total time:** 74.3s  
**Avg generation tok/s:** 46.8  
**Avg effective tok/s:** 7.6  
