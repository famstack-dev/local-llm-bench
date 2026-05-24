# Apple M4 Max / 128GB / 40 GPU cores

**Model:** gemma-4-26b-a4b-it-mlx@4bit  
**Backend:** lmstudio  
**Scenario:** ops-agent (conversation)  

| Turn | Context | Prefill | Gen | Gen tok/s | Effective tok/s | Total | Output |
|-----:|--------:|--------:|----:|----------:|----------------:|------:|-------:|
| 1 | 575 | 0.83s | 1.39s | 103.3 | **64.7** | 2.23s | 144 |
| 2 | 957 | 0.65s | 2.33s | 101.9 | **79.8** | 2.98s | 238 |
| 3 | 1,302 | 0.53s | 2.65s | 101.8 | **84.9** | 3.18s | 270 |
| 4 | 1,783 | 0.66s | 2.67s | 100.9 | **80.9** | 3.33s | 269 |
| 5 | 2,309 | 0.70s | 3.79s | 100.2 | **84.6** | 4.49s | 380 |
| 6 | 2,914 | 0.84s | 2.44s | 100.0 | **74.4** | 3.28s | 244 |
| 7 | 3,249 | 0.52s | 3.60s | 98.4 | **86.1** | 4.11s | 354 |
| 8 | 3,799 | 0.73s | 4.28s | 96.0 | **82.0** | 5.01s | 411 |

**Total prefill:** 5.4s  
**Total generation:** 23.2s  
**Total time:** 28.6s  
**Avg generation tok/s:** 100.3  
**Avg effective tok/s:** 80.7  
