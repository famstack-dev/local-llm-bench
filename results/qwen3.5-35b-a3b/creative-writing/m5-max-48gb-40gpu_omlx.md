# Apple M5 Max / 48GB / 40 GPU cores

**Model:** Qwen3.5-35B-A3B-4bit  
**Backend:** omlx  
**Scenario:** creative-writing (single-shot)  

| Turn | Context | Prefill | Gen | Gen tok/s | Effective tok/s | Total | Output |
|-----:|--------:|--------:|----:|----------:|----------------:|------:|-------:|
| 1 | 57 | 15.36s | 0.00s | 7397.4 | **0.1** | 15.36s | 1 |
| 2 | 60 | 11.57s | 3.50s | 9.4 | **2.2** | 15.07s | 33 |
| 3 | 58 | 15.36s | 0.00s | 8905.1 | **0.1** | 15.36s | 1 |

**Total prefill:** 42.3s  
**Total generation:** 3.5s  
**Total time:** 45.8s  
**Avg generation tok/s:** 5437.3  
**Avg effective tok/s:** 0.8  
