# Apple M2 Max / 64GB / 38 GPU cores

**Model:** Qwen3.6-35B-A3B-UD-MLX-fp16  
**Backend:** omlx  
**Scenario:** creative-writing (single-shot)  
**GPU wired limit:** 59392 MB  

| Turn | Context | Prefill | Gen | Gen tok/s | Effective tok/s | Total | Output |
|-----:|--------:|--------:|----:|----------:|----------------:|------:|-------:|
| 1 | 57 | 24.44s | 2.58s | 8.9 | **0.9** | 27.02s | 23 |
| 2 | 60 | 27.14s | 0.00s | 5645.1 | **0.0** | 27.14s | 1 |
| 3 | 58 | 26.94s | 0.00s | 7307.1 | **0.0** | 26.94s | 1 |

**Total prefill:** 78.5s  
**Total generation:** 2.6s  
**Total time:** 81.1s  
**Avg generation tok/s:** 4320.4  
**Avg effective tok/s:** 0.3  
