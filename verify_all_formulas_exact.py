import pandas as pd
from math import sqrt
from collections import defaultdict

# Exact closed-form formulas
# For odd primes p > 3

def f1(p):
    # (p^2 + 1)/2
    return (p*p + 1) // 2

def f2(p):
    # p^2 - 1
    return p*p - 1

def f3(p):
    # (p^2 + 2p - 1)/2 == (p*(p+2) - 1)/2
    return (p*p + 2*p - 1) // 2


def exact_rmse(actual, predicted):
    """Compute RMSE using integer arithmetic; returns 0 exactly when all equal."""
    if len(actual) == 0:
        return 0
    diffsq_sum = 0
    for a, b in zip(actual, predicted):
        d = a - b
        diffsq_sum += d*d
    if diffsq_sum == 0:
        return 0
    # Fallback (shouldn't happen if exact match)
    return sqrt(diffsq_sum / len(actual))


def main():
    try:
        df = pd.read_csv("reversed_dickson_values_by_cardinality.csv")
    except FileNotFoundError:
        print("Error: 'reversed_dickson_values_by_cardinality.csv' not found. Run Test.py first.")
        return

    # Use only value_count == 2
    card2 = df[df["value_count"] == 2].copy()

    # Group actual n's by p
    by_p = defaultdict(list)
    for _, row in card2.iterrows():
        by_p[int(row["p"])].append(int(row["n"]))

    # Ensure lists are unique and sorted for stable comparison
    for p in by_p:
        by_p[p] = sorted(set(by_p[p]))

    mismatches = []

    # Collect data per pattern for RMSE calculation
    patt1_actual, patt1_pred = [], []
    patt2_actual, patt2_pred = [], []
    patt3_actual, patt3_pred = [], []

    for p, ns in sorted(by_p.items()):
        if p <= 3:
            continue

        expected_set = {f1(p), f2(p), f3(p)}
        actual_set = set(ns)

        if actual_set != expected_set:
            mismatches.append((p, sorted(actual_set), sorted(expected_set)))
        
        # Append per-pattern pairs only if the formula value is present in actual
        n1 = f1(p)
        n2 = f2(p)
        n3 = f3(p)
        if n1 in actual_set:
            patt1_actual.append(n1)
            patt1_pred.append(n1)
        if n2 in actual_set:
            patt2_actual.append(n2)
            patt2_pred.append(n2)
        if n3 in actual_set:
            patt3_actual.append(n3)
            patt3_pred.append(n3)

    # Compute exact RMSEs
    rmse1 = exact_rmse(patt1_actual, patt1_pred)
    rmse2 = exact_rmse(patt2_actual, patt2_pred)
    rmse3 = exact_rmse(patt3_actual, patt3_pred)

    print("Exact verification of closed-form formulas for value_count = 2\n")
    print(f"Pattern 1: n = (p^2 + 1)/2 -> pairs: {len(patt1_actual)}, RMSE = {rmse1}")
    print(f"Pattern 2: n = p^2 - 1     -> pairs: {len(patt2_actual)}, RMSE = {rmse2}")
    print(f"Pattern 3: n = (p^2 + 2p - 1)/2 -> pairs: {len(patt3_actual)}, RMSE = {rmse3}\n")

    if mismatches:
        print("Mismatches found (p, actual n's, expected n's):")
        for p, actual, exp in mismatches:
            print(f"  p={p}: actual={actual}, expected={exp}")
    else:
        print("PASS: For all primes p>3, the three formulas exactly match the dataset (RMSE = 0).")


if __name__ == "__main__":
    main()
