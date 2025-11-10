
import pandas as pd

def print_cardinality_2_indices():
    """
    Reads the dataset and prints all indices 'n' that result in a cardinality of 2,
    grouped by the prime 'p'.
    """
    print("--- Indices 'n' Resulting in Cardinality 2 ---\n")
    
    try:
        df = pd.read_csv("../../data/reversed_dickson_values.csv")
    except FileNotFoundError:
        print("Error: 'data/reversed_dickson_values.csv' not found. Please run the data generation script (scripts/data_generation/Test.py) first.")
        return

    # Filter the DataFrame for rows where the cardinality is 2
    cardinality_2_df = df[df["value_count"] == 2]
    
    if cardinality_2_df.empty:
        print("No instances with a cardinality of 2 were found in the dataset.")
        return

    # Group the results by prime 'p' and print the indices 'n'
    for p, group in cardinality_2_df.groupby('p'):
        n_values = sorted(group['n'].tolist())
        print(f"Prime p = {p}:")
        print(f"  Indices n = {n_values}\n")

if __name__ == "__main__":
    print_cardinality_2_indices()
