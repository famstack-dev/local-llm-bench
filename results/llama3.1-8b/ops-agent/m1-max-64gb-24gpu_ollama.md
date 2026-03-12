# Apple M1 Max / 64GB / 24 GPU cores

**Model:** llama3.1:8b (8.0B, Q4_K_M)  
**Backend:** ollama  
**Scenario:** ops-agent (conversation)  

| Turn | Context | Prefill | Gen | Gen tok/s | Effective tok/s | Total | Output |
|-----:|--------:|--------:|----:|----------:|----------------:|------:|-------:|
| 1 | 575 | 2.26s | 5.32s | 35.5 | 24.9 | 7.58s | 189 |
| 2 | 1,005 | 1.25s | 5.21s | 35.3 | 28.5 | 6.46s | 184 |
| 3 | 1,317 | 0.61s | 4.61s | 34.3 | 30.3 | 5.22s | 158 |
| 4 | 1,710 | 1.05s | 4.00s | 33.5 | 26.5 | 5.05s | 134 |
| 5 | 2,092 | 1.53s | 5.95s | 32.1 | 25.5 | 7.48s | 191 |
| 6 | 2,547 | 1.51s | 3.88s | 30.4 | 21.9 | 5.38s | 118 |
| 7 | 2,797 | 0.60s | 3.89s | 30.3 | 26.3 | 4.49s | 118 |
| 8 | 3,119 | 1.19s | 6.65s | 28.9 | 24.5 | 7.84s | 192 |

**Total prefill:** 10.0s  
**Total generation:** 39.5s  
**Total time:** 49.5s  
**Avg generation tok/s:** 32.5  
**Avg effective tok/s:** 25.9  
