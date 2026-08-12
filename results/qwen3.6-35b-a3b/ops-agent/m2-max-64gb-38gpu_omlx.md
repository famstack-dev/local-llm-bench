# Apple M2 Max / 64GB / 38 GPU cores

**Model:** Qwen3.6-35B-A3B-UD-MLX-fp16  
**Backend:** omlx  
**Scenario:** ops-agent (conversation)  
**GPU wired limit:** 59392 MB  

| Turn | Context | Prefill | Gen | Gen tok/s | Effective tok/s | Total | Output |
|-----:|--------:|--------:|----:|----------:|----------------:|------:|-------:|
| 1 | 575 | 6.42s | 1.40s | 9.3 | **1.7** | 7.83s | 13 |
| 2 | 901 | 1.27s | 1.74s | 9.2 | **5.3** | 3.01s | 16 |
| 3 | 1,140 | 1.48s | 2.51s | 8.8 | **5.5** | 3.99s | 22 |
| 4 | 1,551 | 1.91s | 3.06s | 8.8 | **5.4** | 4.97s | 27 |
| 5 | 2,030 | 2.38s | 3.48s | 8.6 | **5.1** | 5.86s | 30 |
| 6 | 2,529 | 5.73s | 2.04s | 8.8 | **2.3** | 7.77s | 18 |
| 7 | 2,775 | 8.77s | 0.00s | 4788.0 | **0.1** | 8.77s | 1 |
| 8 | 3,431 | 8.14s | 1.03s | 9.7 | **1.1** | 9.17s | 10 |

**Total prefill:** 36.1s  
**Total generation:** 15.3s  
**Total time:** 51.4s  
**Avg generation tok/s:** 606.4  
**Avg effective tok/s:** 2.7  
