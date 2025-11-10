import math
import pandas as pd
import numpy as np


def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    r = int(math.sqrt(n))
    for i in range(3, r+1, 2):
        if n % i == 0:
            return False
    return True


def extract_third_n_non_twin(csv_path="../../data/reversed_dickson_values.csv"):
    df = pd.read_csv(csv_path)
    df2 = df[df["value_count"] == 2]

    data = []  # tuples (p, third_n)

    for p, group in df2.groupby('p'):
        n_values = sorted(group['n'].tolist())

        n1 = (p**2 + 1) // 2
        n2_base = (p**2 - 1) // 2

        remaining = list(n_values)
        # Remove pattern1
        if n1 in remaining:
            remaining.remove(n1)
        # Remove one n that's a multiple of n2_base
        removed_n2 = None
        for n in list(remaining):
            if n2_base > 0 and n % n2_base == 0:
                removed_n2 = n
                remaining.remove(n)
                break

        # Now remaining contains the "third n" values (there may be more than one for p=3)
        # We'll treat non-twin primes only
        if not is_prime(p + 2):
            for n in remaining:
                data.append((p, n))

    return data


def fit_polynomials(points, degrees=(2, 3)):
    # points: list of (p, n)
    xs = np.array([pt[0] for pt in points], dtype=float)
    ys = np.array([pt[1] for pt in points], dtype=float)

    results = {}
    for deg in degrees:
        coeffs = np.polyfit(xs, ys, deg)
        pfunc = np.poly1d(coeffs)
        preds = pfunc(xs)
        residuals = ys - preds
        rmse = float(np.sqrt(np.mean(residuals**2)))
        results[deg] = {
            'coeffs': coeffs.tolist(),
            'rmse': rmse,
            'preds': preds.tolist()
        }
    return results


def pretty_poly_str(coeffs):
    # coeffs list from highest degree to constant
    deg = len(coeffs) - 1
    terms = []
    for i, c in enumerate(coeffs):
        power = deg - i
        c_rounded = round(c, 6)
        if abs(c_rounded) < 1e-12:
            continue
        if power == 0:
            terms.append(f"{c_rounded}")
        elif power == 1:
            terms.append(f"{c_rounded}*p")
        else:
            terms.append(f"{c_rounded}*p**{power}")
    return " + ".join(terms)


def main():
    points = extract_third_n_non_twin()
    if not points:
        print("No non-twin 'third n' points found.")
        return

    # Print points
    print("Non-twin primes and their 'third n' values:")
    for p, n in points:
        print(f"p={p} -> n={n}")

    # Try fitting
    results = fit_polynomials(points, degrees=(2, 3))

    # Save results
    with open('../../output/results/formula_results.txt', 'w') as f:
        f.write("Non-twin primes and their 'third n' values:\n")
        for p, n in points:
            f.write(f"p={p}, n={n}\n")
        f.write('\n')

        for deg, info in results.items():
            coeffs = info['coeffs']
            rmse = info['rmse']
            f.write(f"Degree {deg} fit:\n")
            f.write(f"  Coeffs (highest->const): {coeffs}\n")
            f.write(f"  RMSE: {rmse}\n")
            f.write(f"  Polynomial: n(p) = {pretty_poly_str(coeffs)}\n\n")

    # Also print summary
    print('\nFit results written to output/results/formula_results.txt')
    for deg, info in results.items():
        print(f"Degree {deg} RMSE: {info['rmse']}")
        print(f"Degree {deg} poly: n(p) = {pretty_poly_str(info['coeffs'])}\n")


if __name__ == '__main__':
    main()
