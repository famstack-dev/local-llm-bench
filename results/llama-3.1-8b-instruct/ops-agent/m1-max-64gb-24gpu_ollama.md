# Apple M1 Max / 64GB / 24 GPU cores

**Model:** llama3.1:8b (8.0B, Q4_K_M)  
**Backend:** ollama  
**Scenario:** ops-agent (conversation)  

| Turn | Context | Prefill | Gen | Gen tok/s | Effective tok/s | Total | Output |
|-----:|--------:|--------:|----:|----------:|----------------:|------:|-------:|
| 1 | 575 | 2.12s | 5.13s | 37.6 | **26.6** | 7.25s | 193 |
| 2 | 1,007 | 1.22s | 5.88s | 36.0 | **29.9** | 7.10s | 212 |
| 3 | 1,360 | 0.59s | 4.51s | 34.8 | **30.8** | 5.10s | 157 |
| 4 | 1,742 | 1.02s | 3.18s | 34.2 | **25.9** | 4.21s | 109 |
| 5 | 2,092 | 1.39s | 8.38s | 32.8 | **28.2** | 9.77s | 275 |
| 6 | 2,605 | 1.45s | 4.21s | 31.4 | **23.3** | 5.66s | 132 |
| 7 | 2,877 | 0.59s | 5.76s | 30.7 | **27.9** | 6.35s | 177 |
| 8 | 3,253 | 1.18s | 4.13s | 29.3 | **22.8** | 5.30s | 121 |

**Total prefill:** 9.6s  
**Total generation:** 41.2s  
**Total time:** 50.7s  
**Avg generation tok/s:** 33.4  
**Avg effective tok/s:** 27.1  
