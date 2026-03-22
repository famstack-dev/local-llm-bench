# Apple M3 Max / 128GB / 40 GPU cores

**Model:** llama-3.1-8b-instruct  
**Backend:** lmstudio  
**Scenario:** ops-agent (conversation)  

| Turn | Context | Prefill | Gen | Gen tok/s | Effective tok/s | Total | Output |
|-----:|--------:|--------:|----:|----------:|----------------:|------:|-------:|
| 1 | 575 | 1.19s | 8.65s | 23.3 | **20.5** | 9.85s | 202 |
| 2 | 1,032 | 0.78s | 6.92s | 23.9 | **21.4** | 7.70s | 165 |
| 3 | 1,330 | 0.57s | 5.40s | 23.9 | **21.6** | 5.97s | 129 |
| 4 | 1,677 | 0.67s | 4.77s | 22.8 | **20.0** | 5.44s | 109 |
| 5 | 2,047 | 0.77s | 10.55s | 22.2 | **20.7** | 11.31s | 234 |
| 6 | 2,553 | 0.79s | 5.29s | 23.0 | **20.1** | 6.08s | 122 |
| 7 | 2,808 | 0.45s | 6.53s | 23.0 | **21.5** | 6.98s | 150 |
| 8 | 3,188 | 0.72s | 4.97s | 22.7 | **19.9** | 5.69s | 113 |

**Total prefill:** 5.9s  
**Total generation:** 53.1s  
**Total time:** 59.0s  
**Avg generation tok/s:** 23.1  
**Avg effective tok/s:** 20.7  
