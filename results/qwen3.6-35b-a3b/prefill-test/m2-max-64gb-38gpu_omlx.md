# Apple M2 Max / 64GB / 38 GPU cores

**Model:** Qwen3.6-35B-A3B-UD-MLX-fp16  
**Backend:** omlx  
**Scenario:** prefill-test (single-shot)  
**GPU wired limit:** 59392 MB  

| Turn | Context | Prefill | Gen | Gen tok/s | Effective tok/s | Total | Output |
|-----:|--------:|--------:|----:|----------:|----------------:|------:|-------:|
| 1 | 655 | 2.86s | 0.00s | 7097.0 | **0.3** | 2.86s | 1 |
| 2 | 1,453 | 3.44s | 0.00s | 6250.8 | **0.3** | 3.45s | 1 |
| 3 | 3,015 | 5.12s | 0.00s | 7570.9 | **0.2** | 5.12s | 1 |
| 4 | 8,496 | 15.73s | 0.00s | 5915.8 | **0.1** | 15.73s | 1 |

**Total prefill:** 27.2s  
**Total generation:** 0.0s  
**Total time:** 27.2s  
**Avg generation tok/s:** 6708.6  
**Avg effective tok/s:** 0.1  
