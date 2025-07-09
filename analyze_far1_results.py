import pandas as pd
import glob

# Step 1: Load all parts
files = sorted(glob.glob("far1_results_part*.csv"))
df = pd.concat((pd.read_csv(f) for f in files), ignore_index=True)

# Step 2: Calculate comparisons
far_faster = (df["far1_steps"] < df["half_collatz_steps"]).sum()
equal_steps = (df["far1_steps"] == df["half_collatz_steps"]).sum()
half_faster = (df["half_collatz_steps"] < df["far1_steps"]).sum()

# Step 3: Averages
avg_far = df["far1_steps"].mean()
avg_half = df["half_collatz_steps"].mean()
avg_collatz = df["collatz_steps"].mean()

# Step 4: Max lead
diff = df["half_collatz_steps"] - df["far1_steps"]
max_far_adv = diff.max()
max_half_adv = -diff.min()

# Step 5: Print summary
print(f"FAR-1 faster in      : {far_faster:,}")
print(f"Equal steps in       : {equal_steps:,}")
print(f"Half-Collatz faster in: {half_faster:,}\n")

print(f"FAR-1 faster: {far_faster / len(df):.2%}")
print(f"Equal steps: {equal_steps / len(df):.2%}")
print(f"Half-Collatz faster: {half_faster / len(df):.2%}\n")

print(f"Average steps:")
print(f"FAR-1: {avg_far:.2f}")
print(f"Half-Collatz: {avg_half:.2f}")
print(f"Collatz: {avg_collatz:.2f}\n")

print(f"Max lead of FAR-1 over Half-Collatz: {max_far_adv} steps")
print(f"Max lead of Half-Collatz over FAR-1: {max_half_adv} steps")
