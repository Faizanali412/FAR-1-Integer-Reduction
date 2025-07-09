# 🚀 FAR-1 Integer Reduction

**FAR-1 (Faizan Ali Reduction - Version 1)** is a novel integer reduction algorithm that significantly outperforms the traditional **Collatz** and **Half-Collatz** functions in over **93%** of cases. This repository includes the full research paper, Python source code, step analysis, CSV datasets, and graph visualizations.

---

## 🔢 Algorithm Overview

### ✅ FAR-1 Logic

```python
if n % 3 == 0:
    n = n / 3
else:
    n = n - 1
```

### 🔄 Compared Against:

**Half-Collatz**
```python
if n % 2 == 0:
    n = n / 2
else:
    n = n + 1
```

**Classic Collatz**
```python
if n % 2 == 0:
    n = n / 2
else:
    n = 3 * n + 1
```

---

## 📊 Benchmark Results (n = 1 to 10,000,000)

| Algorithm        | Average Steps | % Faster Cases |
|------------------|----------------|----------------|
| **FAR-1**         | 26.74          | 93.92%         |
| **Half-Collatz**  | 33.20          | 3.47%          |
| **Collatz**       | 155.27         | 0%             |

- ⚡ **FAR-1 faster** in: 9,391,611 cases  
- 🤝 **Equal steps** in: 261,205 cases  
- 🟢 **Half-Collatz faster** in: 347,184 cases  
- 📈 **Max lead of FAR-1:** 25 steps  
- ⚠️ **Max lead of Half-Collatz:** 12 steps (only in 1 case)

---

## 📂 Included Files

| File Name                            | Description                                  |
|-------------------------------------|----------------------------------------------|
| `FAR1_Paper_FaizanAli_tex.pdf`      | 📄 Full research paper (LaTeX exported PDF)   |
| `far1_vs_collatz_halfcollatz_analysis.py` | 🔬 Main test script for graph and summary     |
| `far1_results_graph.png`            | 📊 Line graph comparing average steps         |
| `analyze_far1_results.py`           | 📈 Script to summarize all performance stats  |
| `far1_vs_collatz_10M_split.py`      | 📁 Chunked CSV generator for large dataset    |
| `far1_results_part1-4.csv.zip`      | 📦 Dataset of 10 million numbers split in 4   |
| `README.md`                         | 🧾 This README documentation                  |

---

## 🧪 How to Run

### 🛠 Requirements

```bash
pip install pandas matplotlib
```

### ▶️ Run the Main Script

```bash
python3 far1_vs_collatz_halfcollatz_analysis.py
```

### 📁 Output

- ✅ CSV: `far1_vs_collatz_1M.csv`
- 🖼 PNG Graph: `far1_results_graph.png`

---

## 📈 Performance Highlights

- FAR-1 is significantly smoother and faster than Collatz.
- Reduces computation steps by using simple math (`/3` or `-1`).
- Proven effective across 10 million integers.

---

## 📘 License

This project is licensed under:

```text
Creative Commons Zero v1.0 Universal (CC0 1.0)
```

You can copy, modify, distribute, and use it without asking for permission.  
See [`LICENSE`](LICENSE) file for full terms.

---

## 📬 Author

**Faizan Ali**  
Creator of FAR-1 Algorithm  
GitHub: [@Faizanali412](https://github.com/Faizanali412)
Citation: https://doi.org/10.5281/zenodo.15849781


---

##  Citation

Zenodo: https://doi.org/10.5281/zenodo.15849781

---

## 🌐 GitHub Repository

📍 [https://github.com/Faizanali412/FAR-1-Integer-Reduction](https://github.com/Faizanali412/FAR-1-Integer-Reduction)
