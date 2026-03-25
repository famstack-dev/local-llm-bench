# Apple M3 Max / 128GB / 40 GPU cores

**Model:** JANGQ-AI/Qwen3.5-35B-A3B-JANG_4K  
**Backend:** omlx  
**Scenario:** ops-agent (conversation)  

| Turn | Context | Prefill | Gen | Gen tok/s | Effective tok/s | Total | Output |
|-----:|--------:|--------:|----:|----------:|----------------:|------:|-------:|
| 1 | 575 | 1.93s | 4.96s | 62.9 | **45.3** | 6.89s | 312 |
| 2 | 1,101 | 3.59s | 6.67s | 62.8 | **40.8** | 10.26s | 419 |
| 3 | 1,604 | 1.43s | 7.11s | 62.6 | **52.1** | 8.54s | 445 |
| 4 | 2,251 | 6.72s | 5.26s | 62.1 | **27.3** | 11.99s | 327 |
| 5 | 2,850 | 8.26s | 8.05s | 61.9 | **30.5** | 16.31s | 498 |
| 6 | 3,564 | 2.24s | 5.02s | 61.4 | **42.4** | 7.26s | 308 |
| 7 | 3,960 | 11.77s | 7.95s | 60.7 | **24.5** | 19.71s | 482 |
| 8 | 4,620 | 13.89s | 8.23s | 60.8 | **22.6** | 22.12s | 500 |

**Total prefill:** 49.8s  
**Total generation:** 53.3s  
**Total time:** 103.1s  
**Avg generation tok/s:** 61.9  
**Avg effective tok/s:** 31.9  
