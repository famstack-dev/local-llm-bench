# Apple M1 Max / 64GB / 24 GPU cores

**Model:** Qwen3-30B-A3B-Instruct-2507  
**Backend:** llama-server  
**Scenario:** creative-writing (single-shot)  

| Turn | Context | Prefill | Gen | Gen tok/s | Effective tok/s | Total | Output |
|-----:|--------:|--------:|----:|----------:|----------------:|------:|-------:|
| 1 | 57 | 0.29s | 11.99s | 55.9 | **54.6** | 12.28s | 670 |
| 2 | 60 | 0.22s | 8.76s | 57.0 | **55.6** | 8.97s | 499 |
| 3 | 58 | 0.22s | 10.62s | 56.2 | **55.1** | 10.84s | 597 |

**Total prefill:** 0.7s  
**Total generation:** 31.4s  
**Total time:** 32.1s  
**Avg generation tok/s:** 56.4  
**Avg effective tok/s:** 55.0  
