# Apple M1 Max / 64GB / 24 GPU cores

**Model:** Qwen3.6-35B-A3B-UD-MLX-4bit  
**Backend:** omlx  
**Scenario:** creative-writing (single-shot)  

| Turn | Context | Prefill | Gen | Gen tok/s | Effective tok/s | Total | Output |
|-----:|--------:|--------:|----:|----------:|----------------:|------:|-------:|
| 1 | 57 | 0.37s | 7.76s | 51.3 | **49.0** | 8.13s | 398 |
| 2 | 60 | 0.38s | 15.55s | 50.9 | **49.7** | 15.93s | 792 |
| 3 | 58 | 0.39s | 5.82s | 51.0 | **47.8** | 6.21s | 297 |
| 1 | 57 | 0.37s | 7.76s | 51.2 | **48.8** | 8.13s | 397 |
| 2 | 60 | 0.38s | 14.05s | 50.8 | **49.5** | 14.42s | 714 |
| 3 | 58 | 0.39s | 8.71s | 51.1 | **48.9** | 9.10s | 445 |

**Total prefill:** 2.3s  
**Total generation:** 59.6s  
**Total time:** 61.9s  
**Avg generation tok/s:** 51.1  
**Avg effective tok/s:** 49.1  
