# Research on Dickson Polynomial Value Sets

This project contains scripts, data, and research notes for analyzing the value sets of reversed Dickson polynomials, `D_n(x, 1)`, over finite fields `F_p`.

## Objective

The primary goal is to analyze the cardinality (the number of unique values) of these value sets for various primes `p` and indices `n`, and to identify number-theoretic patterns.

## Key Findings

The research uncovered and numerically verified three distinct formulas for the indices `n` that produce a value set of cardinality 2. For any given prime `p > 3`, the set of these indices is:

1.  **Formula 1:** `n = (p^2 + 1) / 2` → value set {1, p-1}
2.  **Formula 2:** `n = p^2 - 1` → value set {1, 2}
3.  **Formula 3:** `n = (p^2 + 2p - 1) / 2` → value set {1, p-1}

All three formulas were verified with **RMSE = 0** (exact match) across the dataset for primes up to 97.

### General Polynomial Equation

A unified polynomial equation that is satisfied by all three indices is:

```
(n - (p^2 + 1)/2) × (n - (p^2 - 1)) × (n - (p^2 + 2p - 1)/2) = 0
```

For any prime `p > 3`, the three roots of this cubic equation in `n` are precisely the indices that yield a value set of cardinality 2.

## Documentation

### Proofs
- **[Reversed Dickson polynomials: two-point value sets (p>3)](docs/proofs/dickson-two-point-value-sets.md)** - Complete formal proof with discriminant criterion
- [Legacy proof document](docs/proofs/proof_cardinality_2.md) - Earlier proof version

### Methodology
- [Research notes](docs/methodology/research_notes.md) - Detailed research methodology, discovery process, and analysis steps

## How to Run

### 1. Generate Data
```bash
python scripts/data_generation/Test.py
```
This will produce:
- `data/reversed_dickson_values.csv` - Raw data for all primes and indices
- `data/reversed_dickson_values_by_cardinality.csv` - Data sorted by cardinality

### 2. Verify Formulas

**Derive formulas using polynomial regression:**
```bash
python scripts/analysis/derive_all_formulas.py
```

**Run exact verification (RMSE=0):**
```bash
python scripts/verification/verify_all_formulas_exact.py
```

**Verify value sets match theoretical predictions:**
```bash
python scripts/verification/verify_value_sets.py
```
This script computationally confirms that the three special indices produce exactly the value sets predicted by the mathematical proof.

### 3. Visualize Data

**Generate interactive plot:**
```bash
python scripts/visualization/plot_cardinality_2_interactive.py
```
This creates `output/interactive/cardinality_2_indices_interactive.html` with hover details and log/linear scale toggle.

**Generate static scatter plots:**
```bash
python scripts/visualization/plot_scatter.py
```
This creates PNG plots in `output/plots/` for each prime.

### 4. Additional Scripts

**Analysis:**
- `scripts/analysis/analyze_cardinality_2.py` - Initial pattern discovery
- `scripts/analysis/analyze_remaining_patterns.py` - Investigate non-twin prime patterns
- `scripts/analysis/derive_formula.py` - Derive polynomial for specific patterns

**Verification:**
- `scripts/verification/verify_cardinality_2_patterns.py` - Pattern verification

**Utilities:**
- `scripts/utilities/print_cardinality_2_indices.py` - Print all cardinality=2 indices grouped by prime
- `scripts/utilities/print_notes.py` - Print research notes to console

## Project Structure

```
.
├── README.md                                    # This file
├── .gitignore                                   # Git ignore patterns
│
├── scripts/                                     # All Python scripts
│   ├── data_generation/
│   │   └── Test.py                             # Generate Dickson polynomial data
│   ├── analysis/
│   │   ├── analyze_cardinality_2.py            # Initial pattern discovery
│   │   ├── analyze_remaining_patterns.py       # Non-twin prime analysis
│   │   ├── derive_all_formulas.py              # Polynomial regression
│   │   └── derive_formula.py                   # Formula derivation
│   ├── verification/
│   │   ├── verify_all_formulas_exact.py        # Exact RMSE=0 verification
│   │   ├── verify_cardinality_2_patterns.py    # Pattern verification
│   │   └── verify_value_sets.py                # Theoretical value set verification
│   ├── visualization/
│   │   ├── plot_scatter.py                     # Static scatter plots
│   │   ├── plot_cardinality_2_indices.py       # Cardinality 2 plots
│   │   └── plot_cardinality_2_interactive.py   # Interactive HTML plots
│   └── utilities/
│       ├── print_cardinality_2_indices.py      # Print indices
│       └── print_notes.py                      # Print notes
│
├── data/                                        # Generated data files
│   ├── reversed_dickson_values.csv             # Raw data
│   └── reversed_dickson_values_by_cardinality.csv  # Sorted data
│
├── output/                                      # Generated outputs
│   ├── plots/                                  # Static PNG plots
│   ├── interactive/                            # Interactive HTML visualizations
│   └── results/                                # Text results and formulas
│
└── docs/                                        # Documentation
    ├── proofs/                                 # Mathematical proofs
    │   ├── dickson-two-point-value-sets.md    # Formal proof (primary)
    │   └── proof_cardinality_2.md             # Legacy proof
    └── methodology/                            # Research methodology
        └── research_notes.md                   # Detailed research process
```

## Requirements

- Python 3.x
- pandas
- plotly (for interactive plots)
- numpy (for polynomial fitting)

## Installation

```bash
pip install pandas plotly numpy
```

## Quick Start

1. Generate data:
   ```bash
   python scripts/data_generation/Test.py
   ```

2. Verify formulas:
   ```bash
   python scripts/verification/verify_all_formulas_exact.py
   ```

3. Create interactive visualization:
   ```bash
   python scripts/visualization/plot_cardinality_2_interactive.py
   ```

4. Open `output/interactive/cardinality_2_indices_interactive.html` in your browser

## Citation

If you use this research, please cite:
- Repository: [Research-about-Dickson-Polynomial](https://github.com/LukeSaccius/Research-about-Dickson-Polynomial)
- Primary proof: [docs/proofs/dickson-two-point-value-sets.md](docs/proofs/dickson-two-point-value-sets.md)

