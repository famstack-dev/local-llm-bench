# Apple M1 Max / 64GB / 24 GPU cores

**Model:** Qwen3-30B-A3B-Instruct-2507-MLX-4bit  
**Backend:** omlx  
**Scenario:** ops-agent (conversation)  

| Turn | Context | Prefill | Gen | Gen tok/s | Effective tok/s | Total | Output |
|-----:|--------:|--------:|----:|----------:|----------------:|------:|-------:|
| 1 | 575 | 2.30s | 6.57s | 50.4 | **37.3** | 8.87s | 331 |
| 2 | 1,124 | 2.09s | 8.33s | 47.7 | **38.1** | 10.42s | 397 |
| 3 | 1,606 | 1.51s | 5.84s | 45.7 | **36.4** | 7.34s | 267 |
| 4 | 2,070 | 1.80s | 5.45s | 42.4 | **31.9** | 7.25s | 231 |
| 5 | 2,545 | 2.07s | 11.51s | 40.9 | **34.7** | 13.58s | 471 |
| 6 | 3,206 | 2.76s | 7.64s | 38.5 | **28.3** | 10.40s | 294 |
| 7 | 3,591 | 1.84s | 9.44s | 37.1 | **31.0** | 11.28s | 350 |
| 8 | 4,099 | 2.41s | 13.23s | 36.1 | **30.5** | 15.64s | 477 |

**Total prefill:** 16.8s  
**Total generation:** 68.0s  
**Total time:** 84.8s  
**Avg generation tok/s:** 42.4  
**Avg effective tok/s:** 33.2  
