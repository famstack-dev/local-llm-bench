# Apple M1 Max / 64GB / 24 GPU cores

**Model:** Qwen3.5-35B-A3B-4bit-fp16  
**Backend:** omlx  
**Scenario:** creative-writing (single-shot)  

| Turn | Context | Prefill | Gen | Gen tok/s | Effective tok/s | Total | Output |
|-----:|--------:|--------:|----:|----------:|----------------:|------:|-------:|
| 1 | 57 | 0.84s | 6.33s | 69.9 | **61.8** | 7.17s | 443 |
| 2 | 60 | 0.55s | 6.85s | 70.4 | **65.1** | 7.41s | 482 |
| 3 | 58 | 0.57s | 5.18s | 70.4 | **63.4** | 5.76s | 365 |

**Total prefill:** 2.0s  
**Total generation:** 18.4s  
**Total time:** 20.3s  
**Avg generation tok/s:** 70.2  
**Avg effective tok/s:** 63.4  
