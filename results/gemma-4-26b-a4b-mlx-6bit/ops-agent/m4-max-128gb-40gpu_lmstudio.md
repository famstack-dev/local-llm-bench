# Apple M4 Max / 128GB / 40 GPU cores

**Model:** gemma-4-26b-a4b-it-mlx@6bit  
**Backend:** lmstudio  
**Scenario:** ops-agent (conversation)  

| Turn | Context | Prefill | Gen | Gen tok/s | Effective tok/s | Total | Output |
|-----:|--------:|--------:|----:|----------:|----------------:|------:|-------:|
| 1 | 575 | 0.88s | 1.80s | 82.5 | **55.6** | 2.68s | 149 |
| 2 | 956 | 0.69s | 2.92s | 81.6 | **66.1** | 3.60s | 238 |
| 3 | 1,296 | 0.56s | 2.06s | 81.9 | **64.4** | 2.62s | 169 |
| 4 | 1,673 | 0.64s | 3.61s | 80.9 | **68.7** | 4.25s | 292 |
| 5 | 2,224 | 0.76s | 4.08s | 80.6 | **68.0** | 4.84s | 329 |
| 6 | 2,790 | 0.85s | 3.41s | 80.4 | **64.2** | 4.26s | 274 |
| 7 | 3,148 | 0.57s | 4.26s | 79.4 | **70.0** | 4.83s | 338 |
| 8 | 3,684 | 0.76s | 5.33s | 79.0 | **69.1** | 6.09s | 421 |

**Total prefill:** 5.7s  
**Total generation:** 27.5s  
**Total time:** 33.2s  
**Avg generation tok/s:** 80.8  
**Avg effective tok/s:** 66.6  
