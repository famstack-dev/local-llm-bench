# Apple M1 Max / 64GB / 24 GPU cores

**Model:** google/gemma-3-12b  
**Backend:** lmstudio  
**Scenario:** vision-extract (single-shot)  

| Turn | Context | Prefill | Gen | Gen tok/s | Effective tok/s | Total | Output |
|-----:|--------:|--------:|----:|----------:|----------------:|------:|-------:|
| 1 | 1,078 | 4.54s | 6.26s | 28.9 | **16.8** | 10.80s | 181 |
| 2 | 1,078 | 4.56s | 12.18s | 27.5 | **20.0** | 16.74s | 335 |
| 3 | 1,078 | 4.41s | 15.52s | 27.1 | **21.1** | 19.93s | 421 |
| 4 | 1,078 | 4.93s | 16.81s | 27.1 | **21.0** | 21.74s | 456 |
| 5 | 1,078 | 4.32s | 7.41s | 27.8 | **17.6** | 11.72s | 206 |
| 6 | 1,078 | 4.38s | 15.02s | 27.6 | **21.4** | 19.39s | 415 |
| 7 | 1,078 | 4.36s | 14.98s | 27.8 | **21.5** | 19.34s | 416 |
| 8 | 1,078 | 4.32s | 13.33s | 27.6 | **20.9** | 17.65s | 368 |

**Total prefill:** 35.8s  
**Total generation:** 101.5s  
**Total time:** 137.3s  
**Avg generation tok/s:** 27.7  
**Avg effective tok/s:** 20.4  
