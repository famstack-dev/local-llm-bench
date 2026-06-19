# Apple M1 Max / 64GB / 24 GPU cores

**Model:** Qwen3.6-35B-A3B-UD-MLX-4bit  
**Backend:** omlx  
**Scenario:** prefill-test (single-shot)  

| Turn | Context | Prefill | Gen | Gen tok/s | Effective tok/s | Total | Output |
|-----:|--------:|--------:|----:|----------:|----------------:|------:|-------:|
| 1 | 655 | 2.09s | 2.46s | 50.4 | **27.2** | 4.55s | 124 |
| 2 | 1,453 | 4.08s | 2.48s | 48.8 | **18.4** | 6.56s | 121 |
| 3 | 3,015 | 4.47s | 2.74s | 48.1 | **18.3** | 7.21s | 132 |
| 4 | 8,496 | 4.20s | 3.30s | 41.5 | **18.3** | 7.50s | 137 |
| 1 | 655 | 2.07s | 1.75s | 50.3 | **23.0** | 3.82s | 88 |
| 2 | 1,453 | 4.08s | 2.85s | 50.1 | **20.6** | 6.93s | 143 |
| 3 | 3,015 | 4.46s | 2.32s | 47.8 | **16.4** | 6.79s | 111 |
| 4 | 8,496 | 4.16s | 2.25s | 41.9 | **14.7** | 6.40s | 94 |

**Total prefill:** 29.6s  
**Total generation:** 20.2s  
**Total time:** 49.8s  
**Avg generation tok/s:** 47.4  
**Avg effective tok/s:** 19.1  
