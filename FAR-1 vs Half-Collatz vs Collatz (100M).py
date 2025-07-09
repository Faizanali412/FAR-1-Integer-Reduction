import csv
import time
import matplotlib.pyplot as plt
import pandas as pd

def collatz_steps(n):
    steps = 0
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        steps += 1
    return steps

def half_collatz_steps(n):
    steps = 0
    while n != 1:
        n = n // 2 if n % 2 == 0 else n + 1
        steps += 1
    return steps

def far1_steps(n):
    steps = 0
    while n != 1:
        n = n // 3 if n % 3 == 0 else n - 1
        steps += 1
    return steps

def run_test_100M():
    far_faster = 0
    half_faster = 0
    equal = 0
    total_far = total_half = total_col = 0

    print("⏳ Starting: n = 1 to 100,000,000")
    t0 = time.time()

    for n in range(1, 100_000_001):
        col = collatz_steps(n)
        half = half_collatz_steps(n)
        far = far1_steps(n)

        total_col += col
        total_half += half
        total_far += far

        if far < half:
            far_faster += 1
        elif half < far:
            half_faster += 1
        else:
            equal += 1

        if n % 10_000_000 == 0:
            print(f"✅ Processed: {n}")

    t1 = time.time()
    print(f"✅ Finished in {round(t1 - t0, 2)} seconds\n")

    # Compute averages
    avg_far = round(total_far / 100_000_000, 4)
    avg_half = round(total_half / 100_000_000, 4)
    avg_col = round(total_col / 100_000_000, 4)

    # Print results to terminal
    print("📊 Summary Results (n = 1 to 100,000,000):")
    print(f"FAR-1 faster        : {far_faster}")
    print(f"Half-Collatz faster : {half_faster}")
    print(f"Equal steps         : {equal}")
    print(f"\nAverage Steps:")
    print(f"FAR-1        : {avg_far}")
    print(f"Half-Collatz : {avg_half}")
    print(f"Collatz      : {avg_col}")

    # Save to CSV
    csv_file = "far1_summary_100M.csv"
    with open(csv_file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["range_start", "range_end", "FAR-1 faster", "Half faster", "Equal",
                         "Avg FAR", "Avg Half", "Avg Collatz"])
        writer.writerow([1, 100_000_000, far_faster, half_faster, equal, avg_far, avg_half, avg_col])
    
    print(f"📁 Summary saved to {csv_file}")

    # Plot bar graph
    labels = ["FAR-1", "Half-Collatz", "Collatz"]
    averages = [avg_far, avg_half, avg_col]

    plt.figure(figsize=(8, 5))
    bars = plt.bar(labels, averages, color=["blue", "green", "red"])
    plt.title("Average Steps (n = 1 to 100,000,000)")
    plt.ylabel("Average Steps")
    plt.ylim(0, max(averages) + 20)

    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2.0, height + 1, f"{height:.2f}", ha='center', va='bottom')

    plt.tight_layout()
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    graph_file = "far1_vs_collatz_halfcollatz_100M_graph.png"
    plt.savefig(graph_file)
    print(f"📊 Graph saved as {graph_file}")
    plt.show()

run_test_100M()
