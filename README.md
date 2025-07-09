# FAR-1: Faizan Ali Reduction — A Fast Integer Reduction Algorithm

A novel integer reduction method that outperforms both Collatz and Half-Collatz algorithms in over **95% of cases** from `n = 1` to `100,000,000`.

---

## Algorithm Description

### FAR-1 Logic
```python
while n != 1:
    if n % 3 == 0:
        n = n // 3
    else:
        n -= 1
```

### Compared Against

**Half-Collatz:**
```python
while n != 1:
    if n % 2 == 0:
        n = n // 2
    else:
        n += 1
```

**Classic Collatz:**
```python
while n != 1:
    if n % 2 == 0:
        n = n // 2
    else:
        n = 3 * n + 1
```

---

## Summary Results (n = 1 to 100,000,000)

- **FAR-1 faster:** 95,382,954 numbers (95.38%)
- **Equal steps:** 1,983,893 numbers (1.98%)
- **Half-Collatz faster:** 2,633,153 numbers (2.63%)

### Average Steps:
- **FAR-1:** 30.91
- **Half-Collatz:** 38.17
- **Collatz:** 179.23

---

## How to Run

### Requirements
- Python 3.8+
- pandas
- matplotlib

### Install dependencies
```bash
pip install pandas matplotlib
```

### Run comparison code (for 100 million integers)
```bash
python3 far1_vs_collatz_halfcollatz_analysis.py
```

### Outputs
- `far1_summary_100M.csv` — step results summary
- `far1_vs_collatz_halfcollatz_100M_graph.png` — graph comparison of average steps

---

## 📁 Files Included

- `far1_vs_collatz_halfcollatz_analysis.py` — Main test script
- `far1_results_part1.csv.zip` to `part4` — Full test data for 10M chunks
- `far1_results_graph.png` — Visualization of average step count
- `FAR1_Paper_FaizanAli_tex.pdf` — Formal research paper
- `README.md` — You’re reading it!
- `LICENSE` — CC0 1.0 Universal License (Public Domain)

---

## 📌 Citation

If you use this work, please cite:
```
Faizan Ali. "FAR-1: A Fast Integer Reduction Method Compared to Collatz and Half-Collatz." 2025. https://doi.org/10.5281/zenodo.15849781
```

---

## 🌐 Links

- GitHub: [FAR-1 Repository](https://github.com/Faizanali412/FAR-1-Integer-Reduction)
- Zenodo DOI: [10.5281/zenodo.15849781](https://doi.org/10.5281/zenodo.15849781)

---

## Author

**Faizan Ali**  
Inventor of FAR-1  
[LinkedIn](https://www.linkedin.com/in/faizan-ali-a32052149/) | [GitHub](https://github.com/Faizanali412)
