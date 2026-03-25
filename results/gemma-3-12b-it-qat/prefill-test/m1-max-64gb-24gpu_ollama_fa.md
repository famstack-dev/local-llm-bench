# Apple M1 Max / 64GB / 24 GPU cores

**Model:** gemma3:12b-it-qat (12.2B, Q4_0)  
**Backend:** ollama  
**Scenario:** prefill-test (single-shot)  
**Ollama config:** flash_attention=1  

| Turn | Context | Prefill | Gen | Gen tok/s | Effective tok/s | Total | Output |
|-----:|--------:|--------:|----:|----------:|----------------:|------:|-------:|
| 1 | 655 | 3.44s | 4.18s | 19.6 | **10.7** | 7.63s | 82 |
| 2 | 1,453 | 7.45s | 7.43s | 20.2 | **10.1** | 14.88s | 150 |
| 3 | 3,015 | 17.71s | 8.26s | 18.2 | **5.8** | 25.98s | 150 |
| 4 | 8,496 | 76.03s | 11.56s | 13.0 | **1.7** | 87.59s | 150 |

**Total prefill:** 104.6s  
**Total generation:** 31.4s  
**Total time:** 136.1s  
**Avg generation tok/s:** 17.8  
**Avg effective tok/s:** 3.9  
