import pandas as pd
import os

def run_analysis():
    # Construct paths dynamically to avoid directory issues
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(base_dir, 'data', 'india_historical_birth_death_imr_1947_2026.csv')
    
    if not os.path.exists(file_path):
        print(f"❌ Error: Data file not found at {file_path}. Please check your folder layout.")
        return

    # Load dataset
    df = pd.read_csv(file_path)
    
    print("\n==============================================")
    print("📈 HISTORICAL DATA OVERVIEW (1947 - 2026)")
    print("==============================================")
    print(f"Total Rows Captured: {df.shape[0]}")
    print(f"Tracked States: {', '.join(df['State'].unique())}")
    
    print("\n📊 NATIONAL & STATE LEVEL SUMMARY STATISTICS:")
    print(df.describe().round(2))
    
    # Target specific year summary
    target_year = 2026
    print(f"\n📍 STATE-WISE SNAPSHOT FOR THE YEAR: {target_year}")
    df_year = df[df['Year'] == target_year]
    print(df_year[['State', 'Live_Births', 'Total_Deaths', 'Infant_Mortality_Rate_IMR']].to_string(index=False))
    
    # Historical Progress Tracker for Maharashtra
    print("\n📉 HISTORICAL IMR PROGRESSION TRACKER (MAHARASHTRA):")
    df_mh = df[df['State'] == 'Maharashtra'].sort_values(by='Year')
    milestones = [1947, 1970, 1990, 2010, 2026]
    df_milestones = df_mh[df_mh['Year'].isin(milestones)]
    print(df_milestones[['Year', 'Live_Births', 'Total_Deaths', 'Infant_Mortality_Rate_IMR']].to_string(index=False))

if __name__ == "__main__":
    run_analysis()
