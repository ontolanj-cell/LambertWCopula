from import_data import load_data
from summary_statistics import summary_statistics
from scatter_plot import create_scatter_plot
from pseudo_observations import create_pseudo_observations
from correlations import correlation_analysis
from empirical_copula import empirical_copula

print("="*60)
print("Lambert W Copula Analysis System")
print("="*60)

# Load data
data = load_data("Temp_Precipitation.csv")

# Summary
summary_statistics(data)

# Scatter plot
create_scatter_plot(data)

# Pseudo observations
pseudo = create_pseudo_observations(data)

# Correlations
correlation_analysis(data)

# Empirical copula
empirical_copula(pseudo)

print("\nAnalysis Completed Successfully!")