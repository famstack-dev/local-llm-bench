# Apple M1 Max / 64GB / 24 GPU cores

**Model:** Qwen3-30B-A3B-Instruct-2507  
**Backend:** llama-server  
**Scenario:** ops-agent (conversation)  

| Turn | Context | Prefill | Gen | Gen tok/s | Effective tok/s | Total | Output |
|-----:|--------:|--------:|----:|----------:|----------------:|------:|-------:|
| 1 | 575 | 1.39s | 3.59s | 53.2 | **38.4** | 4.98s | 191 |
| 2 | 973 | 0.96s | 8.40s | 49.6 | **44.5** | 9.37s | 417 |
| 3 | 1,459 | 0.48s | 5.73s | 47.8 | **44.2** | 6.21s | 274 |
| 4 | 1,930 | 0.78s | 5.76s | 47.2 | **41.6** | 6.54s | 272 |
| 5 | 2,429 | 0.84s | 10.28s | 45.3 | **41.9** | 11.12s | 466 |
| 6 | 3,064 | 1.14s | 7.44s | 44.8 | **38.8** | 8.58s | 333 |
| 7 | 3,466 | 0.55s | 10.81s | 43.7 | **41.6** | 11.36s | 473 |
| 8 | 4,103 | 0.88s | 11.60s | 42.8 | **39.8** | 12.47s | 496 |

**Total prefill:** 7.0s  
**Total generation:** 63.6s  
**Total time:** 70.6s  
**Avg generation tok/s:** 46.8  
**Avg effective tok/s:** 41.4  
