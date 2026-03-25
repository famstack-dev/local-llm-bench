# Apple M1 Max / 64GB / 24 GPU cores

**Model:** Qwen3.5-35B-A3B-4bit-fp16  
**Backend:** omlx  
**Scenario:** ops-agent (conversation)  

| Turn | Context | Prefill | Gen | Gen tok/s | Effective tok/s | Total | Output |
|-----:|--------:|--------:|----:|----------:|----------------:|------:|-------:|
| 1 | 575 | 1.53s | 4.05s | 67.4 | **48.9** | 5.58s | 273 |
| 2 | 1,076 | 2.56s | 6.07s | 68.0 | **47.9** | 8.62s | 413 |
| 3 | 1,612 | 2.04s | 4.72s | 66.8 | **46.7** | 6.75s | 315 |
| 4 | 2,133 | 1.50s | 4.25s | 64.4 | **47.7** | 5.75s | 274 |
| 5 | 2,659 | 2.57s | 7.63s | 62.8 | **47.0** | 10.20s | 479 |
| 6 | 3,349 | 2.50s | 5.23s | 64.2 | **43.5** | 7.73s | 336 |
| 7 | 3,776 | 1.62s | 6.90s | 64.6 | **52.3** | 8.52s | 446 |
| 8 | 4,401 | 2.81s | 7.21s | 63.2 | **45.5** | 10.03s | 456 |

**Total prefill:** 17.1s  
**Total generation:** 46.1s  
**Total time:** 63.2s  
**Avg generation tok/s:** 65.2  
**Avg effective tok/s:** 47.3  
