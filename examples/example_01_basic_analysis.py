"""
Example 1

Basic Lambert W Copula Analysis
"""

from lambertwcopula import *

# Load data
data = load_csv("../data/data.csv")

# Preprocessing
u, v = pseudo_observations(data)

# Fit model
result = fit_optimizer(u, v)

print(result)

print()

print("Theta:", result.theta)

print("LogLik:", result.loglik)

print("AIC:", result.aic)

print("BIC:", result.bic)