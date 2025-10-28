
import pandas as pd

def verify_cardinality_2_patterns():
    """
    Verifies the discovered patterns for indices 'n' where the cardinality is 2.
    """
    print("Verifying patterns for indices 'n' where cardinality is 2...\n")
    
    try:
        df = pd.read_csv("reversed_dickson_values.csv")
    except FileNotFoundError:
        print("Error: 'reversed_dickson_values.csv' not found. Please run the data generation script first.")
        return

    cardinality_2_df = df[df["value_count"] == 2]
    primes = sorted(cardinality_2_df["p"].unique())

    if not primes:
        print("No instances with cardinality 2 found in the data.")
        return

    for p in primes:
        print(f"--- Verifying for prime p = {p} ---")
        
        n_values = sorted(cardinality_2_df[cardinality_2_df["p"] == p]["n"].tolist())
        print(f"  Observed n values: {n_values}")

        # --- Verification 1: The (p^2 + 1) / 2 formula ---
        # This formula is expected to hold for p > 3
        if p > 3:
            formula_n1 = (p**2 + 1) / 2
            if formula_n1 in n_values:
                print(f"  [PASS] Found n = (p^2 + 1) / 2 = {int(formula_n1)}")
            else:
                print(f"  [FAIL] Did not find n = (p^2 + 1) / 2 = {int(formula_n1)}")
        else:
            print("  [INFO] Skipping (p^2 + 1) / 2 check for p=3 (known exception).")

        # --- Verification 2: The multiple of (p^2 - 1) / 2 pattern ---
        formula_n2_base = (p**2 - 1) / 2
        found_multiple = False
        for n in n_values:
            if n > 0 and n % formula_n2_base == 0:
                multiple = n / formula_n2_base
                print(f"  [PASS] Found n = {n}, which is {int(multiple)} * (p^2 - 1) / 2")
                found_multiple = True
                break
        
        if not found_multiple:
            print(f"  [FAIL] Did not find any n that is a multiple of (p^2 - 1) / 2 = {int(formula_n2_base)}")
        
        print("-" * (28 + len(str(p))))
        print()

if __name__ == "__main__":
    verify_cardinality_2_patterns()
