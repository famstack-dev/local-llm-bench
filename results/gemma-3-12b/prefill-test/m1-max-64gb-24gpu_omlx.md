# Apple M1 Max / 64GB / 24 GPU cores

**Model:** gemma-3-12b-it-qat-4bit  
**Backend:** omlx  
**Scenario:** prefill-test (single-shot)  

| Turn | Context | Prefill | Gen | Gen tok/s | Effective tok/s | Total | Output |
|-----:|--------:|--------:|----:|----------:|----------------:|------:|-------:|
| 1 | 655 | 5.60s | 2.77s | 25.2 | **8.4** | 8.38s | 70 |
| 2 | 1,453 | 13.04s | 5.96s | 25.2 | **7.9** | 19.00s | 150 |
| 3 | 3,015 | 29.01s | 6.13s | 24.5 | **4.3** | 35.14s | 150 |
| 4 | 8,496 | 115.81s | 7.96s | 18.8 | **1.2** | 123.77s | 150 |

**Total prefill:** 163.5s  
**Total generation:** 22.8s  
**Total time:** 186.3s  
**Avg generation tok/s:** 23.4  
**Avg effective tok/s:** 2.8  
