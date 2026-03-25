# Apple M2 Pro / 32GB / 19 GPU cores

**Model:** GLM-4.7-Flash-4bit  
**Backend:** omlx  
**Scenario:** ops-agent (conversation)  

| Turn | Context | Prefill | Gen | Gen tok/s | Effective tok/s | Total | Output |
|-----:|--------:|--------:|----:|----------:|----------------:|------:|-------:|
| 1 | 575 | 2.73s | 5.66s | 40.7 | **27.4** | 8.38s | 230 |
| 2 | 1,052 | 2.45s | 4.63s | 38.6 | **25.3** | 7.08s | 179 |
| 3 | 1,331 | 1.94s | 5.01s | 38.1 | **27.5** | 6.95s | 191 |
| 4 | 1,735 | 1.92s | 4.98s | 38.0 | **27.4** | 6.90s | 189 |
| 5 | 2,172 | 2.90s | 9.44s | 35.3 | **27.0** | 12.34s | 333 |
| 6 | 2,728 | 2.90s | 4.67s | 35.5 | **21.9** | 7.57s | 166 |
| 7 | 2,993 | 2.11s | 3.30s | 34.0 | **20.7** | 5.41s | 112 |
| 8 | 3,292 | 2.65s | 6.60s | 33.3 | **23.8** | 9.25s | 220 |

**Total prefill:** 19.6s  
**Total generation:** 44.3s  
**Total time:** 63.9s  
**Avg generation tok/s:** 36.7  
**Avg effective tok/s:** 25.4  
