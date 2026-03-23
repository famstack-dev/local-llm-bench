# Apple M3 Max / 128GB / 40 GPU cores

**Model:** Qwen3.5-35B-A3B-4bit  
**Backend:** omlx  
**Scenario:** prefill-test (single-shot)  

| Turn | Context | Prefill | Gen | Gen tok/s | Effective tok/s | Total | Output |
|-----:|--------:|--------:|----:|----------:|----------------:|------:|-------:|
| 1 | 655 | 0.64s | 1.51s | 93.2 | **65.4** | 2.16s | 141 |
| 2 | 1,453 | 1.21s | 1.61s | 93.2 | **53.2** | 2.82s | 150 |
| 3 | 3,015 | 2.78s | 1.37s | 88.4 | **29.2** | 4.15s | 121 |
| 4 | 8,496 | 13.06s | 1.64s | 76.7 | **8.6** | 14.70s | 126 |

**Total prefill:** 17.7s  
**Total generation:** 6.1s  
**Total time:** 23.8s  
**Avg generation tok/s:** 87.9  
**Avg effective tok/s:** 22.6  
