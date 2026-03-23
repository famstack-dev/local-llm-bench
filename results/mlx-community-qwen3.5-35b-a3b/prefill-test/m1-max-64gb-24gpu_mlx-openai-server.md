# Apple M1 Max / 64GB / 24 GPU cores

**Model:** /Users/merlin/.lmstudio/models/mlx-community/Qwen3.5-35B-A3B-4bit  
**Backend:** mlx-openai-server  
**Scenario:** prefill-test (single-shot)  

| Turn | Context | Prefill | Gen | Gen tok/s | Effective tok/s | Total | Output |
|-----:|--------:|--------:|----:|----------:|----------------:|------:|-------:|
| 1 | 655 | 2.31s | 2.10s | 60.6 | **28.8** | 4.41s | 127 |
| 2 | 1,453 | 4.30s | 2.42s | 59.1 | **21.3** | 6.72s | 143 |
| 3 | 3,015 | 9.21s | 2.30s | 58.6 | **11.7** | 11.51s | 135 |
| 4 | 8,496 | 38.21s | 2.86s | 51.7 | **3.6** | 41.08s | 148 |

**Total prefill:** 54.0s  
**Total generation:** 9.7s  
**Total time:** 63.7s  
**Avg generation tok/s:** 57.5  
**Avg effective tok/s:** 8.7  
