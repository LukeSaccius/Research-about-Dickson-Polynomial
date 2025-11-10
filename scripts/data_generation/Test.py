import math
import pandas as pd

# List odd primes up to 97
primes = []
for p in range(3, 98, 2):
    isprime = True
    for q in range(3, int(math.sqrt(p)) + 1, 2):
        if p % q == 0:
            isprime = False
            break
    if isprime:
        primes.append(p)

data = []
for p in primes:
    # Compute D_n(1, x) for x = 0..p-1 via recurrence in F_p
    Dprev = [2] * p  # D_0(1, x) = 2
    Dcurr = [1] * p  # D_1(1, x) = 1
    # Record n = 0
    vals = sorted(set(Dprev))
    data.append((p, 0, len(vals), len(vals) == p, vals))
    # Record n = 1
    vals = sorted(set(Dcurr))
    data.append((p, 1, len(vals), len(vals) == p, vals))
    # For n >= 2
    for n in range(2, p * p):
        Dnext = []
        for x in range(p):
            Dnext_val = (Dcurr[x] - x * Dprev[x]) % p
            Dnext.append(Dnext_val)
        vals = sorted(set(Dnext))
        data.append((p, n, len(vals), len(vals) == p, vals))
        Dprev, Dcurr = Dcurr, Dnext

# Build DataFrame and display it
df = pd.DataFrame(data, columns=["p", "n", "value_count", "is_permutation", "values"])
print("Reversed Dickson value sets (a = 1):")
with pd.option_context("display.max_rows", None, "display.max_columns", None, "display.width", None):
    print(df)

# Save a CSV-friendly copy
df_for_csv = df.copy()
df_for_csv["values"] = df_for_csv["values"].apply(lambda lst: ",".join(str(v) for v in lst))
df_for_csv.to_csv("../../data/reversed_dickson_values.csv", index=False)
print('Saved results to "data/reversed_dickson_values.csv".')

# Sort by cardinality (descending) then save a separate CSV
df_sorted = df.sort_values(["value_count", "p", "n"], ascending=[False, True, True]).reset_index(drop=True)
df_sorted_for_csv = df_sorted.copy()
df_sorted_for_csv["values"] = df_sorted_for_csv["values"].apply(lambda lst: ",".join(str(v) for v in lst))
df_sorted_for_csv.to_csv("../../data/reversed_dickson_values_by_cardinality.csv", index=False)
print('Saved sorted results to "data/reversed_dickson_values_by_cardinality.csv".')
