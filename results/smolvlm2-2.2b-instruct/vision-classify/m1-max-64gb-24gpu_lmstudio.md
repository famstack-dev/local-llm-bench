# Apple M1 Max / 64GB / 24 GPU cores

**Model:** smolvlm2-2.2b-instruct  
**Backend:** lmstudio  
**Scenario:** vision-classify (single-shot)  

| Turn | Context | Prefill | Gen | Gen tok/s | Effective tok/s | Total | Output |
|-----:|--------:|--------:|----:|----------:|----------------:|------:|-------:|
| 1 | 1,136 | 0.82s | 0.83s | 107.8 | **54.2** | 1.66s | 90 |
| 2 | 1,136 | 0.91s | 0.71s | 110.1 | **48.3** | 1.61s | 78 |
| 3 | 1,136 | 0.82s | 0.75s | 108.9 | **52.2** | 1.57s | 82 |
| 4 | 1,136 | 1.49s | 0.71s | 110.5 | **35.8** | 2.21s | 79 |
| 5 | 1,136 | 0.65s | 0.84s | 106.5 | **59.9** | 1.49s | 89 |
| 6 | 1,136 | 0.65s | 0.77s | 108.4 | **58.5** | 1.42s | 83 |
| 7 | 1,136 | 0.73s | 0.80s | 109.1 | **56.8** | 1.53s | 87 |
| 8 | 1,136 | 0.69s | 0.61s | 113.1 | **53.1** | 1.30s | 69 |

**Total prefill:** 6.8s  
**Total generation:** 6.0s  
**Total time:** 12.8s  
**Avg generation tok/s:** 109.3  
**Avg effective tok/s:** 51.4  
