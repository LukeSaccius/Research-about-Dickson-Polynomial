# Research on Dickson Polynomial Value Sets

This project contains scripts and research notes for analyzing the value sets of reversed Dickson polynomials, `D_n(x, 1)`, over finite fields `F_p`.

## Objective

The primary goal is to analyze the cardinality (the number of unique values) of these value sets for various primes `p` and indices `n`, and to identify number-theoretic patterns.

## Key Findings

The research uncovered several key patterns, particularly for cases where the cardinality of the value set is 2. For a given prime `p > 3`, the set of indices `n` that produce a cardinality of 2 consistently includes:

1.  `n = (p^2 + 1) / 2`
2.  `n = p^2 - 1`
3.  A third value that is conditional on `p`'s status as a twin prime:
    *   If `p+2` is prime, `n = (p*(p+2) - 1) / 2`.
    *   Otherwise, `n` follows a more complex, undetermined pattern.

For a full breakdown of the methodology and analysis, please see `research_notes.md`.

## How to Run

1.  **Generate Data:**
    ```bash
    python Test.py
    ```
    This will produce the `reversed_dickson_values.csv` file.

2.  **Generate Scatter Plots:**
    ```bash
    python plot_scatter.py
    ```

3.  **Analyze Cardinality Patterns:**
    ```bash
    python analyze_cardinality_2.py
    python verify_cardinality_2_patterns.py
    python analyze_remaining_patterns.py
    ```
