# Apple M5 Max / 48GB / 40 GPU cores

**Model:** llama3.1:8b (8.0B, Q4_K_M)  
**Backend:** ollama  
**Scenario:** ops-agent (conversation)  

| Turn | Context | Prefill | Gen | Gen tok/s | Effective tok/s | Total | Output |
|-----:|--------:|--------:|----:|----------:|----------------:|------:|-------:|
| 1 | 575 | 0.42s | 1.87s | 84.5 | **69.0** | 2.29s | 158 |
| 2 | 979 | 0.28s | 1.91s | 76.6 | **66.7** | 2.19s | 146 |
| 3 | 1,250 | 0.23s | 2.37s | 76.0 | **69.3** | 2.60s | 180 |
| 4 | 1,672 | 0.31s | 1.88s | 70.3 | **60.3** | 2.19s | 132 |
| 5 | 2,067 | 0.33s | 2.02s | 73.2 | **63.1** | 2.35s | 148 |
| 6 | 2,497 | 0.36s | 1.42s | 70.7 | **56.4** | 1.77s | 100 |
| 7 | 2,740 | 0.21s | 1.53s | 71.4 | **62.7** | 1.74s | 109 |
| 8 | 3,066 | 0.33s | 2.03s | 69.3 | **59.6** | 2.37s | 141 |

**Total prefill:** 2.5s  
**Total generation:** 15.0s  
**Total time:** 17.5s  
**Avg generation tok/s:** 74.0  
**Avg effective tok/s:** 63.7  
