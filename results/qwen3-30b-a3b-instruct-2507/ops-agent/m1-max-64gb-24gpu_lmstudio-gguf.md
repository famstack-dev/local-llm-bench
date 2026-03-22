# Apple M1 Max / 64GB / 24 GPU cores

**Model:** qwen3-30b-a3b-instruct-2507  
**Backend:** lmstudio-gguf  
**Scenario:** ops-agent (conversation)  

| Turn | Context | Prefill | Gen | Gen tok/s | Effective tok/s | Total | Output |
|-----:|--------:|--------:|----:|----------:|----------------:|------:|-------:|
| 1 | 575 | 1.46s | 4.51s | 54.5 | **41.2** | 5.97s | 246 |
| 2 | 1,034 | 1.05s | 7.22s | 51.3 | **44.7** | 8.27s | 370 |
| 3 | 1,488 | 0.58s | 5.83s | 49.9 | **45.4** | 6.41s | 291 |
| 4 | 1,989 | 0.87s | 4.23s | 48.7 | **40.4** | 5.10s | 206 |
| 5 | 2,436 | 0.94s | 10.18s | 46.7 | **42.7** | 11.12s | 475 |
| 6 | 3,078 | 1.27s | 6.29s | 46.1 | **38.4** | 7.55s | 290 |
| 7 | 3,464 | 0.64s | 8.12s | 45.1 | **41.8** | 8.76s | 366 |
| 8 | 4,008 | 0.97s | 11.11s | 43.2 | **39.7** | 12.08s | 480 |

**Total prefill:** 7.8s  
**Total generation:** 57.5s  
**Total time:** 65.3s  
**Avg generation tok/s:** 48.2  
**Avg effective tok/s:** 41.7  
