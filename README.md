# Research on Dickson Polynomial Value Sets

This project contains scripts and research notes for analyzing the value sets of reversed Dickson polynomials, `D_n(x, 1)`, over finite fields `F_p`.

## Objective

The primary goal is to analyze the cardinality (the number of unique values) of these value sets for various primes `p` and indices `n`, and to identify number-theoretic patterns.

## Key Findings

The research uncovered and numerically verified three distinct formulas for the indices `n` that produce a value set of cardinality 2. For any given prime `p > 3`, the set of these indices is:

1.  **Formula 1:** `n = (p^2 + 1) / 2` → value set {1, p-1}
2.  **Formula 2:** `n = p^2 - 1` → value set {1, 2}
3.  **Formula 3:** `n = (p^2 + 2p - 1) / 2` → value set {1, p-1}

All three formulas were verified with **RMSE = 0** (exact match) across the dataset for primes up to 97.

**For a complete mathematical proof**, see [proof_cardinality_2.md](proof_cardinality_2.md).

### General Polynomial Equation

A unified polynomial equation that is satisfied by all three indices is:

```
(n - (p^2 + 1)/2) × (n - (p^2 - 1)) × (n - (p^2 + 2p - 1)/2) = 0
```

For any prime `p > 3`, the three roots of this cubic equation in `n` are precisely the indices that yield a value set of cardinality 2.

For a full breakdown of the methodology, analysis, and theoretical explanations, please see `research_notes.md`.

## How to Run

### 1. Generate Data
```bash
python Test.py
```
This will produce:
- `reversed_dickson_values.csv` - Raw data for all primes and indices
- `reversed_dickson_values_by_cardinality.csv` - Data sorted by cardinality

### 2. Verify Formulas

**Derive formulas using polynomial regression:**
```bash
python derive_all_formulas.py
```

**Run exact verification (RMSE=0):**
```bash
python verify_all_formulas_exact.py
```

**Verify value sets match theoretical predictions:**
```bash
python verify_value_sets.py
```
This script computationally confirms that the three special indices produce exactly the value sets predicted by the mathematical proof.

### 3. Visualize Data

**Generate interactive plot:**
```bash
python plot_cardinality_2_interactive.py
```
This creates `cardinality_2_indices_interactive.html` with hover details and log/linear scale toggle.

### 4. Additional Analysis Scripts

- `analyze_cardinality_2.py` - Initial pattern discovery
- `verify_cardinality_2_patterns.py` - Pattern verification
- `print_cardinality_2_indices.py` - Print all cardinality=2 indices grouped by prime

## Project Structure

```
.
├── Test.py                              # Data generation
├── derive_all_formulas.py               # Polynomial regression on all patterns
├── verify_all_formulas_exact.py         # Exact verification (RMSE=0)
├── verify_value_sets.py                 # Verify theoretical value sets
├── plot_cardinality_2_interactive.py    # Interactive visualization
├── proof_cardinality_2.md               # Complete mathematical proof
├── research_notes.md                    # Detailed methodology and findings
├── README.md                            # This file
└── [analysis scripts]                   # Additional exploration tools
```

## Requirements

- Python 3.x
- pandas
- plotly (for interactive plots)
- numpy (for polynomial fitting)
