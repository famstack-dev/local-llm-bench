# Apple M1 Max / 64GB / 24 GPU cores

**Model:** /Users/merlin/.lmstudio/models/mlx-community/Qwen3.5-35B-A3B-4bit  
**Backend:** mlx-openai-server  
**Scenario:** creative-writing (single-shot)  

| Turn | Context | Prefill | Gen | Gen tok/s | Effective tok/s | Total | Output |
|-----:|--------:|--------:|----:|----------:|----------------:|------:|-------:|
| 1 | 57 | 0.71s | 7.04s | 62.8 | **57.0** | 7.75s | 442 |
| 2 | 60 | 0.61s | 11.50s | 62.3 | **59.2** | 12.11s | 717 |
| 3 | 58 | 0.62s | 4.76s | 63.0 | **55.8** | 5.38s | 300 |

**Total prefill:** 1.9s  
**Total generation:** 23.3s  
**Total time:** 25.2s  
**Avg generation tok/s:** 62.7  
**Avg effective tok/s:** 57.8  
