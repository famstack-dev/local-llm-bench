# Apple M1 Max / 64GB / 24 GPU cores

**Model:** /Users/merlin/.lmstudio/models/mlx-community/Qwen3.5-35B-A3B-4bit  
**Backend:** mlx-openai-server  
**Scenario:** doc-summary (single-shot)  

| Turn | Context | Prefill | Gen | Gen tok/s | Effective tok/s | Total | Output |
|-----:|--------:|--------:|----:|----------:|----------------:|------:|-------:|
| 1 | 425 | 1.87s | 1.92s | 59.4 | **30.1** | 3.79s | 114 |
| 2 | 612 | 1.76s | 1.37s | 59.2 | **25.9** | 3.13s | 81 |
| 3 | 535 | 1.95s | 1.78s | 59.6 | **28.4** | 3.73s | 106 |
| 4 | 524 | 1.86s | 1.90s | 60.7 | **30.6** | 3.75s | 115 |
| 5 | 1,518 | 3.98s | 1.93s | 60.1 | **19.6** | 5.91s | 116 |

**Total prefill:** 11.4s  
**Total generation:** 8.9s  
**Total time:** 20.3s  
**Avg generation tok/s:** 59.8  
**Avg effective tok/s:** 26.2  
