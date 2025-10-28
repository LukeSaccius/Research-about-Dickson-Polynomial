
import matplotlib.pyplot as plt
import pandas as pd

# Load the data
df = pd.read_csv("reversed_dickson_values.csv")

# Get the unique primes
primes = df["p"].unique()

# Create a scatter plot for each prime
for p in primes:
    prime_data = df[df["p"] == p]
    plt.figure(figsize=(10, 6))
    plt.scatter(prime_data["n"], prime_data["value_count"], alpha=0.5)
    plt.title(f"Cardinality vs. Index (n) for p={p}")
    plt.xlabel("Index (n)")
    plt.ylabel("Cardinality of Value Set")
    plt.grid(True)
    plt.savefig(f"scatter_p_{p}.png")
    plt.close()

print("Scatter plots generated for all primes.")
