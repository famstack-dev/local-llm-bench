# Apple M1 Max / 64GB / 24 GPU cores

**Model:** mlx-community/Qwen3.5-35B-A3B-4bit  
**Backend:** rapid-mlx  
**Scenario:** ops-agent (conversation)  

| Turn | Context | Prefill | Gen | Gen tok/s | Effective tok/s | Total | Output |
|-----:|--------:|--------:|----:|----------:|----------------:|------:|-------:|
| 1 | 575 | 2.27s | 4.87s | 60.5 | **41.3** | 7.15s | 295 |
| 2 | 1,088 | 4.45s | 5.71s | 60.8 | **34.2** | 10.16s | 347 |
| 3 | 1,529 | 3.85s | 5.30s | 60.5 | **35.1** | 9.15s | 321 |
| 4 | 2,071 | 3.49s | 4.37s | 61.1 | **34.0** | 7.86s | 267 |
| 5 | 2,578 | 3.84s | 6.09s | 59.7 | **36.6** | 9.93s | 364 |
| 6 | 3,158 | 4.34s | 4.91s | 59.1 | **31.3** | 9.25s | 290 |
| 7 | 3,539 | 3.90s | 5.58s | 59.1 | **34.8** | 9.48s | 330 |
| 8 | 4,072 | 3.48s | 6.47s | 58.6 | **38.1** | 9.95s | 379 |

**Total prefill:** 29.6s  
**Total generation:** 43.3s  
**Total time:** 72.9s  
**Avg generation tok/s:** 59.9  
**Avg effective tok/s:** 35.6  
