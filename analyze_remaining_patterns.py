
import pandas as pd
import math

def is_prime(num):
    """Checks if a number is prime."""
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def analyze_remaining_patterns():
    """
    Analyzes the 'third' n value for primes that are NOT part of a twin prime pair.
    """
    print("Analyzing the remaining 'n' values for non-twin primes...\n")
    
    try:
        df = pd.read_csv("reversed_dickson_values.csv")
    except FileNotFoundError:
        print("Error: 'reversed_dickson_values.csv' not found.")
        return

    cardinality_2_df = df[df["value_count"] == 2]
    primes = sorted(cardinality_2_df["p"].unique())

    remaining_n_values = {}

    for p in primes:
        n_values = set(cardinality_2_df[cardinality_2_df["p"] == p]["n"].tolist())
        
        # Remove the two known patterns
        n1 = (p**2 + 1) / 2
        n2_base = (p**2 - 1) / 2
        
        n_values.discard(n1)
        
        # Find and remove the multiple of n2_base
        n2_multiple = -1
        for n_val in list(n_values):
            if n_val > 0 and n_val % n2_base == 0:
                n2_multiple = n_val
                break
        if n2_multiple != -1:
            n_values.discard(n2_multiple)

        # Check if p is the first in a twin prime pair
        if not is_prime(p + 2):
            if n_values:
                # We are left with the n values for non-twin primes
                remaining_n_values[p] = list(n_values)

    print("--- Analysis for Non-Twin Primes ---")
    if not remaining_n_values:
        print("No remaining 'n' values found for non-twin primes.")
        return

    # Let's check for a new pattern related to p^2
    for p, n_list in remaining_n_values.items():
        for n in n_list:
            print(f"For p = {p}, remaining n = {n}")
            
            # Hypothesis: Is n related to (p^2 - p) / 2 or similar?
            # Let's test a new formula: n = (p^2 - p + 2) / 2
            formula_n3 = (p**2 - p + 2) / 2
            if n == formula_n3:
                print(f"  [PASS] Matches formula: n = (p^2 - p + 2) / 2 = {int(formula_n3)}")
            else:
                print(f"  [FAIL] Does not match formula (p^2 - p + 2) / 2. Formula gives {int(formula_n3)}")

if __name__ == "__main__":
    analyze_remaining_patterns()
