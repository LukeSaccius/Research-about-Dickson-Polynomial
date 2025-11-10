
import pandas as pd
import numpy as np

def is_prime(num):
    """Checks if a number is prime."""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def get_twin_primes(max_p):
    """Get a set of twin primes up to a certain limit."""
    primes = {i for i in range(2, max_p + 1) if is_prime(i)}
    twin_primes = set()
    for p in primes:
        if p + 2 in primes:
            twin_primes.add(p)
    return twin_primes

def pretty_poly_str(coeffs):
    """Creates a human-readable string for a polynomial from its coefficients."""
    parts = []
    # np.polyfit returns coeffs from highest power to lowest, so we iterate normally
    for i, c in enumerate(coeffs):
        if abs(c) < 1e-9:  # Skip near-zero coefficients
            continue
        power = len(coeffs) - 1 - i
        term = f"{c:.2f}"
        if power > 0:
            term += "*p"
        if power > 1:
            term += f"**{power}"
        parts.append(term)
    return " + ".join(parts).replace(" + -", " - ")

def fit_and_print_poly(name, data, degree=2):
    """Fits a polynomial to the data and prints the results."""
    if not data:
        print(f"--- {name} ---")
        print("No data points to fit.\n")
        return

    ps, ns = zip(*data)
    ps = np.array(ps)
    ns = np.array(ns)

    coeffs = np.polyfit(ps, ns, degree)
    p_func = np.poly1d(coeffs)
    
    # Calculate RMSE
    y_pred = p_func(ps)
    rmse = np.sqrt(np.mean((ns - y_pred)**2))

    print(f"--- {name} ---")
    print(f"Data points: {len(data)}")
    print(f"Derived Formula: n(p) = {pretty_poly_str(coeffs)}")
    print(f"RMSE: {rmse:.4f}\n")


def main():
    # Load data
    try:
        df = pd.read_csv("../../data/reversed_dickson_values_by_cardinality.csv")
    except FileNotFoundError:
        print("Error: 'data/reversed_dickson_values_by_cardinality.csv' not found.")
        print("Please run Test.py to generate the data.")
        return

    # Filter for value_count 2
    card2_df = df[df['value_count'] == 2].copy()
    
    # Group by prime
    grouped = card2_df.groupby('p')['n'].apply(list).to_dict()

    max_p = card2_df['p'].max()
    twin_primes = get_twin_primes(max_p)

    # Prepare lists for each pattern
    pattern1_data = [] # n = (p^2+1)/2
    pattern2_data = [] # n = p^2-1
    pattern3_twin_data = [] # "Third n" for twin primes
    pattern3_nontwin_data = [] # "Third n" for non-twin primes

    for p, ns in grouped.items():
        if p <= 3:
            continue

        # Expected values based on our formulas
        n1_expected = (p**2 + 1) / 2
        n2_expected = p**2 - 1
        
        remaining_ns = set(ns)

        # Identify and categorize n1 and n2
        for n_val in ns:
            if abs(n_val - n1_expected) < 1e-9:
                pattern1_data.append((p, n_val))
                remaining_ns.discard(n_val)
            elif abs(n_val - n2_expected) < 1e-9:
                pattern2_data.append((p, n_val))
                remaining_ns.discard(n_val)

        # The remaining n is the "third n"
        if remaining_ns:
            third_n = remaining_ns.pop()
            if p in twin_primes:
                pattern3_twin_data.append((p, third_n))
            else:
                pattern3_nontwin_data.append((p, third_n))

    print("Deriving Polynomial Formulas for All Cardinality=2 Patterns\n")
    fit_and_print_poly("Pattern 1: (p^2+1)/2", pattern1_data)
    fit_and_print_poly("Pattern 2: p^2-1", pattern2_data)
    fit_and_print_poly("Pattern 3 (Twin Primes)", pattern3_twin_data)
    fit_and_print_poly("Pattern 3 (Non-Twin Primes)", pattern3_nontwin_data)


if __name__ == "__main__":
    main()
