import os
import pandas as pd

def run_analysis():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(base_dir, "data", "india_historical_birth_death_imr_1947_2026.csv")
    
    if not os.path.exists(file_path):
        print(f"Error: Data file not found at {file_path}.")
        return

    df = pd.read_csv(file_path)
    print("\n==============================================")
    print("📈 HISTORICAL DATA OVERVIEW (1947 - 2026)")
    print("==============================================")
    print(f"Total Rows: {df.shape[0]}")
    print(f"Tracked States: {', '.join(df['State'].unique())}\n")
    print(df.describe().round(2))

if __name__ == "__main__":
    run_analysis()
