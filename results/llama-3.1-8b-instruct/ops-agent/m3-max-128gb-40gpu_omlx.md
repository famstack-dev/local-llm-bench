# Apple M3 Max / 128GB / 40 GPU cores

**Model:** Llama-3.1-8B-Instruct  
**Backend:** omlx  
**Scenario:** ops-agent (conversation)  

| Turn | Context | Prefill | Gen | Gen tok/s | Effective tok/s | Total | Output |
|-----:|--------:|--------:|----:|----------:|----------------:|------:|-------:|
| 1 | 575 | 1.04s | 2.74s | 72.6 | **52.6** | 3.78s | 199 |
| 2 | 1,021 | 0.90s | 2.77s | 73.2 | **55.2** | 3.68s | 203 |
| 3 | 1,358 | 0.67s | 2.67s | 71.2 | **57.0** | 3.33s | 190 |
| 4 | 1,780 | 0.65s | 2.21s | 69.7 | **53.9** | 2.86s | 154 |
| 5 | 2,207 | 1.06s | 3.79s | 67.6 | **52.8** | 4.85s | 256 |
| 6 | 2,716 | 0.88s | 1.65s | 67.7 | **44.3** | 2.53s | 112 |
| 7 | 2,970 | 0.46s | 2.65s | 67.8 | **57.8** | 3.12s | 180 |
| 8 | 3,373 | 0.80s | 2.94s | 65.7 | **51.6** | 3.74s | 193 |

**Total prefill:** 6.5s  
**Total generation:** 21.4s  
**Total time:** 27.9s  
**Avg generation tok/s:** 69.4  
**Avg effective tok/s:** 53.3  
