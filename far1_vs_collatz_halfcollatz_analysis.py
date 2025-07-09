import pandas as pd
import matplotlib.pyplot as plt

# === Define the 3 Methods ===
def far_1(n):
    steps = 0
    while n != 1:
        if n % 3 == 0:
            n //= 3
        else:
            n -= 1
        steps += 1
    return steps

def collatz(n):
    steps = 0
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        steps += 1
    return steps

def half_collatz(n):
    steps = 0
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n += 1
        steps += 1
    return steps

# === Run Tests from 1 to 10,000,000 ===
data = {"n": [], "FAR-1": [], "Collatz": [], "Half-Collatz": []}

for i in range(1, 10_000_001):
    data["n"].append(i)
    data["FAR-1"].append(far_1(i))
    data["Collatz"].append(collatz(i))
    data["Half-Collatz"].append(half_collatz(i))

df = pd.DataFrame(data)
df.to_csv("far1_vs_collatz_1M.csv", index=False)

# === Plot Results ===
df["group"] = df["n"] // 1000
avg_steps = df.groupby("group")[["FAR-1", "Collatz", "Half-Collatz"]].mean()

plt.figure(figsize=(12, 6))
plt.plot(avg_steps["FAR-1"], label="FAR-1", color="blue")
plt.plot(avg_steps["Collatz"], label="Collatz", color="red")
plt.plot(avg_steps["Half-Collatz"], label="Half-Collatz", color="green")
plt.title("Average Steps from n = 1 to 10,000,000 (Grouped by 1000s)")
plt.xlabel("Group Number (Each Group = 1000 values)")
plt.ylabel("Average Steps")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("far1_vs_collatz_plot_10M.png")
plt.show()
