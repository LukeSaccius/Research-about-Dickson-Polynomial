
import pandas as pd
import matplotlib.pyplot as plt

def plot_cardinality_2_indices():
    """
    Creates a scatter plot of indices 'n' that result in cardinality 2,
    grouped by prime 'p' and color-coded by the discovered patterns.
    """
    print("Generating plot for indices 'n' where cardinality is 2...")
    
    try:
        df = pd.read_csv("../../data/reversed_dickson_values.csv")
    except FileNotFoundError:
        print("Error: 'data/reversed_dickson_values.csv' not found. Please run the data generation script (scripts/data_generation/Test.py) first.")
        return

    cardinality_2_df = df[df["value_count"] == 2]
    
    if cardinality_2_df.empty:
        print("No instances with a cardinality of 2 were found.")
        return

    primes = sorted(cardinality_2_df['p'].unique())
    
    # Lists to hold data for each pattern
    pattern1_p, pattern1_n = [], []  # n = (p^2 + 1) / 2
    pattern2_p, pattern2_n = [], []  # n = k * (p^2 - 1) / 2
    pattern3_p, pattern3_n = [], []  # The "third n"

    for p in primes:
        n_values = set(cardinality_2_df[cardinality_2_df["p"] == p]["n"].tolist())
        
        # Identify and categorize each n
        n1 = (p**2 + 1) / 2
        n2_base = (p**2 - 1) / 2
        
        # Pattern 1
        if n1 in n_values:
            pattern1_p.append(p)
            pattern1_n.append(n1)
            n_values.discard(n1)
            
        # Pattern 2
        n2_multiple = -1
        for n in list(n_values):
            if n > 0 and n % n2_base == 0:
                n2_multiple = n
                break
        if n2_multiple != -1:
            pattern2_p.append(p)
            pattern2_n.append(n2_multiple)
            n_values.discard(n2_multiple)
            
        # Pattern 3 (whatever is left)
        if n_values:
            for n in n_values:
                pattern3_p.append(p)
                pattern3_n.append(n)

    # Create the plot
    plt.figure(figsize=(14, 10))
    
    plt.scatter(pattern1_p, pattern1_n, label='Pattern 1: n = (p² + 1) / 2', alpha=0.8)
    plt.scatter(pattern2_p, pattern2_n, label='Pattern 2: n = k * (p² - 1) / 2', alpha=0.8)
    plt.scatter(pattern3_p, pattern3_n, label='Pattern 3: The "Third n" (Conditional)', alpha=0.8)
    
    plt.title('Indices n giving Cardinality 2 vs. Prime p', fontsize=16)
    plt.xlabel('Prime (p)', fontsize=12)
    plt.ylabel('Index (n)', fontsize=12)
    plt.legend()
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.yscale('log') # Use a logarithmic scale for y-axis as n grows quadratically
    
    # Save the plot
    plt.savefig('../../output/plots/cardinality_2_indices_plot.png')
    print("Plot saved as 'output/plots/cardinality_2_indices_plot.png'")
    plt.close()

if __name__ == "__main__":
    plot_cardinality_2_indices()
