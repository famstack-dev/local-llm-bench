# Apple M2 Pro / 32GB / 19 GPU cores

**Model:** qwen3.5-35b-a3b  
**Backend:** lmstudio  
**Scenario:** creative-writing (single-shot)  

| Turn | Context | Prefill | Gen | Gen tok/s | Effective tok/s | Total | Output |
|-----:|--------:|--------:|----:|----------:|----------------:|------:|-------:|
| 1 | 57 | 3.79s | 6.32s | 62.8 | **39.3** | 10.11s | 397 |
| 2 | 60 | 3.75s | 11.41s | 62.2 | **46.8** | 15.16s | 710 |
| 3 | 58 | 3.70s | 6.95s | 62.6 | **40.9** | 10.65s | 435 |

**Total prefill:** 11.2s  
**Total generation:** 24.7s  
**Total time:** 35.9s  
**Avg generation tok/s:** 62.5  
**Avg effective tok/s:** 42.9  
