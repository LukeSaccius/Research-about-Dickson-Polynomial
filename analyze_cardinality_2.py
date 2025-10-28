
import pandas as pd

# Load the data
df = pd.read_csv("reversed_dickson_values.csv")

# Filter for cardinality 2
cardinality_2_df = df[df["value_count"] == 2]

# Get the unique primes where cardinality 2 occurs
primes = cardinality_2_df["p"].unique()

# Dictionary to hold the results
n_sequences = {}

# Find the sequence of n for each prime
for p in sorted(primes):
    prime_data = cardinality_2_df[cardinality_2_df["p"] == p]
    n_values = sorted(prime_data["n"].tolist())
    n_sequences[p] = n_values

# Print the sequences and analyze them
for p, n_values in n_sequences.items():
    print(f"For prime p = {p}, indices n with cardinality 2 are:")
    print(n_values)
    
    # Basic analysis: Check for arithmetic progression
    if len(n_values) > 1:
        # Check for patterns related to p
        p_plus_1 = p + 1
        p_minus_1 = p - 1
        
        print(f"  p+1 = {p_plus_1}, p-1 = {p_minus_1}")

        for n in n_values:
            if n % p_plus_1 == 0:
                print(f"    n = {n} is a multiple of p+1")
            if n % p_minus_1 == 0:
                print(f"    n = {n} is a multiple of p-1")
    else:
        print("  -> Not enough data points to determine a sequence.\n")

if not n_sequences:
    print("No instances found with a cardinality of 2.")

