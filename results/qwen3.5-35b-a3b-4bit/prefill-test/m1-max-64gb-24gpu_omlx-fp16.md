# Apple M1 Max / 64GB / 24 GPU cores

**Model:** Qwen3.5-35B-A3B-4bit-fp16  
**Backend:** omlx  
**Scenario:** prefill-test (single-shot)  

| Turn | Context | Prefill | Gen | Gen tok/s | Effective tok/s | Total | Output |
|-----:|--------:|--------:|----:|----------:|----------------:|------:|-------:|
| 1 | 655 | 1.48s | 2.10s | 67.9 | **39.9** | 3.58s | 143 |
| 2 | 1,453 | 2.76s | 2.21s | 67.0 | **29.8** | 4.97s | 148 |
| 3 | 3,015 | 5.71s | 1.97s | 64.1 | **16.4** | 7.67s | 126 |
| 4 | 8,496 | 24.16s | 2.11s | 51.2 | **4.1** | 26.27s | 108 |

**Total prefill:** 34.1s  
**Total generation:** 8.4s  
**Total time:** 42.5s  
**Avg generation tok/s:** 62.5  
**Avg effective tok/s:** 12.4  
