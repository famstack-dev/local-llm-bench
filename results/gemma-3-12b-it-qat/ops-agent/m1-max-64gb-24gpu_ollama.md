# Apple M1 Max / 64GB / 24 GPU cores

**Model:** gemma3:12b-it-qat (12.2B, Q4_0)  
**Backend:** ollama  
**Scenario:** ops-agent (conversation)  

| Turn | Context | Prefill | Gen | Gen tok/s | Effective tok/s | Total | Output |
|-----:|--------:|--------:|----:|----------:|----------------:|------:|-------:|
| 1 | 575 | 3.68s | 5.44s | 18.6 | **11.1** | 9.12s | 101 |
| 2 | 886 | 3.02s | 6.88s | 18.2 | **12.6** | 9.89s | 125 |
| 3 | 1,125 | 7.99s | 8.45s | 18.4 | **9.4** | 16.43s | 155 |
| 4 | 1,490 | 10.32s | 8.44s | 17.2 | **7.7** | 18.76s | 145 |
| 5 | 1,887 | 12.72s | 9.10s | 17.1 | **7.1** | 21.82s | 156 |
| 6 | 2,269 | 15.77s | 5.97s | 17.3 | **4.7** | 21.74s | 103 |
| 7 | 2,478 | 17.01s | 7.80s | 16.4 | **5.2** | 24.81s | 128 |
| 8 | 2,776 | 19.33s | 8.16s | 16.4 | **4.9** | 27.49s | 134 |

**Total prefill:** 89.8s  
**Total generation:** 60.2s  
**Total time:** 150.1s  
**Avg generation tok/s:** 17.4  
**Avg effective tok/s:** 7.0  
