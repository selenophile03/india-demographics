import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def generate_trends():
    current_script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root_dir = os.path.dirname(current_script_dir)
    
    file_path = os.path.join(project_root_dir, 'data', 'india_historical_birth_death_imr_1947_2026.csv')
    output_image = os.path.join(project_root_dir, 'statewise_imr_trends_1947_2026.png')
    
    if not os.path.exists(file_path):
        print(f"❌ Error: Data source layout not found at path: {file_path}")
        return

    df = pd.read_csv(file_path)
    
    plt.figure(figsize=(11, 6), dpi=300)
    sns.set_theme(style="whitegrid")
    
    sns.lineplot(
        data=df, 
        x='Year', 
        y='Infant_Mortality_Rate_IMR', 
        hue='State', 
        linewidth=2.5
    )
    
    plt.title('Historical Infant Mortality Rate (IMR) Trends Across States (1947 - 2026)', fontsize=13, fontweight='bold', pad=15)
    plt.xlabel('Year', fontsize=11, fontweight='bold')
    plt.ylabel('IMR (Deaths per 1,000 Live Births)', fontsize=11, fontweight='bold')
    plt.xlim(1947, 2026)
    
    plt.legend(title='🇮🇳 Indian States', loc='upper right', bbox_to_anchor=(1.25, 1))
    plt.tight_layout()
    
    plt.savefig(output_image, bbox_inches='tight')
    print(f"✅ Success! Chart image generated and saved to: {output_image}")
    plt.close()

if __name__ == "__main__":
    generate_trends()
