# Apple M1 Max / 64GB / 24 GPU cores

**Model:** /Users/merlin/.lmstudio/models/mlx-community/Qwen3.5-35B-A3B-4bit  
**Backend:** mlx-openai-server  
**Scenario:** ops-agent (conversation)  

| Turn | Context | Prefill | Gen | Gen tok/s | Effective tok/s | Total | Output |
|-----:|--------:|--------:|----:|----------:|----------------:|------:|-------:|
| 1 | 575 | 2.29s | 3.51s | 59.8 | **36.2** | 5.80s | 210 |
| 2 | 1,019 | 3.73s | 6.28s | 58.8 | **36.9** | 10.01s | 369 |
| 3 | 1,482 | 5.05s | 6.77s | 59.6 | **34.2** | 11.83s | 404 |
| 4 | 2,095 | 6.73s | 4.33s | 60.5 | **23.7** | 11.06s | 262 |
| 5 | 2,620 | 8.02s | 7.68s | 60.2 | **29.4** | 15.70s | 462 |
| 6 | 3,329 | 10.31s | 4.65s | 59.1 | **18.4** | 14.96s | 275 |
| 7 | 3,706 | 11.23s | 6.47s | 59.0 | **21.6** | 17.70s | 382 |
| 8 | 4,289 | 13.05s | 8.49s | 57.2 | **22.6** | 21.54s | 486 |

**Total prefill:** 60.4s  
**Total generation:** 48.2s  
**Total time:** 108.6s  
**Avg generation tok/s:** 59.3  
**Avg effective tok/s:** 26.2  
