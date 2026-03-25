# Apple M1 Max / 64GB / 24 GPU cores

**Model:** gemma-3-12b-it-qat-4bit  
**Backend:** omlx  
**Scenario:** ops-agent (conversation)  

| Turn | Context | Prefill | Gen | Gen tok/s | Effective tok/s | Total | Output |
|-----:|--------:|--------:|----:|----------:|----------------:|------:|-------:|
| 1 | 575 | 6.05s | 3.33s | 25.3 | **9.0** | 9.37s | 84 |
| 2 | 887 | 9.80s | 19.63s | 25.5 | **17.0** | 29.44s | 500 |
| 3 | 1,322 | 7.51s | 19.25s | 26.0 | **18.7** | 26.77s | 500 |
| 4 | 1,885 | 6.33s | 3.71s | 25.6 | **9.5** | 10.04s | 95 |
| 5 | 2,169 | 9.61s | 19.50s | 25.6 | **17.2** | 29.11s | 500 |
| 6 | 2,660 | 9.49s | 0.18s | 11.3 | **0.2** | 9.66s | 2 |
| 7 | 2,759 | 3.27s | 0.40s | 22.6 | **2.5** | 3.67s | 9 |
| 8 | 2,960 | 5.47s | 20.05s | 24.9 | **19.6** | 25.52s | 500 |

**Total prefill:** 57.5s  
**Total generation:** 86.0s  
**Total time:** 143.6s  
**Avg generation tok/s:** 23.4  
**Avg effective tok/s:** 15.3  
