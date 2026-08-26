import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def generate_trends():
    # Setup paths
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(base_dir, 'data', 'india_historical_birth_death_imr_1947_2026.csv')
    output_image = os.path.join(base_dir, 'statewise_imr_trends_1947_2026.png')
    
    if not os.path.exists(file_path):
        print(f"❌ Error: Data file missing at {file_path}")
        return

    # Load and configure setup
    df = pd.read_csv(file_path)
    plt.figure(figsize=(14, 7), dpi=300)
    sns.set_theme(style="whitegrid")
    
    # Plot line mappings
    sns.lineplot(
        data=df, 
        x='Year', 
        y='Infant_Mortality_Rate_IMR', 
        hue='State', 
        linewidth=2.5,
        marker='o',
        markevery=10
    )
    
    # Visual Polish
    plt.title('Historical Infant Mortality Rate (IMR) Downward Trends (1947 - 2026)', fontsize=14, fontweight='bold', pad=15)
    plt.xlabel('Timeline (Years)', fontsize=12, fontweight='bold')
    plt.ylabel('IMR (Deaths per 1,000 Live Births)', fontsize=12, fontweight='bold')
    plt.xlim(1947, 2026)
    plt.ylim(0, df['Infant_Mortality_Rate_IMR'].max() + 10)
    
    plt.legend(title='🇮🇳 Indian States', title_fontsize='11', loc='upper right', bbox_to_anchor=(1.20, 1))
    plt.tight_layout()
    
    # Save chart output
    plt.savefig(output_image, bbox_inches='tight')
    print(f"✅ Success: Analytical chart safely plotted and saved to: {output_image}")
    plt.close()

if __name__ == "__main__":
    generate_trends()
