import pandas as pd
import os

def run_analysis():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(base_dir, 'data', 'india_historical_birth_death_imr_1947_2026.csv')
    
    if not os.path.exists(file_path):
        print(f"❌ Error: Data file not found at {file_path}.")
        return

    df = pd.read_csv(file_path)
    
    print("\n==============================================")
    print("📈 HISTORICAL DATA OVERVIEW (1947 - 2026)")
    print("==============================================")
    print(f"Total Rows Captured: {df.shape[0]}")
    print(f"Tracked States: {', '.join(df['State'].unique())}")
    
    print("\n📊 NATIONAL & STATE LEVEL SUMMARY STATISTICS:")
    print(df.describe().round(2))
    
    target_year = 2026
    print(f"\n📍 STATE-WISE SNAPSHOT FOR THE YEAR: {target_year}")
    df_year = df[df['Year'] == target_year]
    print(df_year[['State', 'Live_Births', 'Total_Deaths', 'Infant_Mortality_Rate_IMR']].to_string(index=False))

if __name__ == "__main__":
    run_analysis()
