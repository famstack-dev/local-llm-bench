# Apple M1 Max / 64GB / 24 GPU cores

**Model:** llama3.1:8b (8.0B, Q4_K_M)  
**Backend:** ollama  
**Scenario:** prefill-test (single-shot)  

| Turn | Context | Prefill | Gen | Tok/s | Total | Output |
|-----:|--------:|--------:|----:|------:|------:|-------:|
| 1 | 655 | 2.37s | 2.97s | 35.4 | 5.34s | 105 |
| 2 | 1,453 | 4.98s | 4.50s | 33.4 | 9.47s | 150 |
| 3 | 3,015 | 11.65s | 5.06s | 29.7 | 16.71s | 150 |
| 4 | 8,496 | 60.09s | 7.77s | 19.3 | 67.86s | 150 |

**Total prefill:** 79.1s  
**Total generation:** 20.3s  
**Total time:** 99.4s  
**Avg generation tok/s:** 29.4  
