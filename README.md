# FAR-1-Integer-Reduction
A novel integer reduction algorithm (FAR-1) that outperforms Collatz and Half-Collatz in over 93% of cases. Includes full research paper, Python code, benchmarks, and analysis.


FAR-1 is a newly proposed integer reduction method that significantly outperforms the traditional Collatz and Half-Collatz functions. This repository includes all source code, dataset, graphs, and the research paper submitted to arXiv.

---

## 🔢 Algorithm Description

### FAR-1 Logic
If `n % 3 == 0`:  
  `n = n / 3`  
Else:  
  `n = n - 1`

### Compared Against:

#### Half-Collatz
If `n % 2 == 0`: `n = n / 2`  
Else: `n = n + 1`

#### Classic Collatz
If `n % 2 == 0`: `n = n / 2`  
Else: `n = 3n + 1`

---

## 📊 Results Summary (n = 1 to 10,000,000)

- FAR-1 faster in: **9,391,611 cases** (93.92%)
- Equal steps in: **261,205 cases** (2.61%)
- Half-Collatz faster in: **347,184 cases** (3.47%)

### Average Steps:
- FAR-1: **26.74**
- Half-Collatz: **33.20**
- Collatz: **155.27**

### Max Advantage:
- FAR-1: **25 steps faster**
- Half-Collatz: **12 steps faster** (only in 1 case)

---

## 🧪 How to Run

Requirements:
- Python 3.8+
- `pandas`
- `matplotlib`

```bash
pip install pandas matplotlib
python3 far1_vs_collatz.py
