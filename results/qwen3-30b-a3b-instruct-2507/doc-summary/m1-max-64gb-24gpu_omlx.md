# Apple M1 Max / 64GB / 24 GPU cores

**Model:** Qwen3-30B-A3B-Instruct-2507-MLX-4bit  
**Backend:** omlx  
**Scenario:** doc-summary (single-shot)  

| Turn | Context | Prefill | Gen | Gen tok/s | Effective tok/s | Total | Output |
|-----:|--------:|--------:|----:|----------:|----------------:|------:|-------:|
| 1 | 425 | 1.85s | 1.97s | 52.2 | **26.9** | 3.82s | 103 |
| 2 | 612 | 1.75s | 1.56s | 50.8 | **23.9** | 3.31s | 79 |
| 3 | 535 | 1.91s | 1.83s | 51.4 | **25.1** | 3.74s | 94 |
| 4 | 524 | 1.85s | 1.99s | 52.2 | **27.1** | 3.84s | 104 |
| 5 | 1,518 | 4.47s | 3.09s | 46.5 | **19.0** | 7.57s | 144 |

**Total prefill:** 11.8s  
**Total generation:** 10.4s  
**Total time:** 22.3s  
**Avg generation tok/s:** 50.6  
**Avg effective tok/s:** 23.5  
