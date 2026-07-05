"""
Lambert W Copula Analysis
=========================

Main Program
"""

import numpy as np

from lambertwcopula import *

print("=" * 70)
print("Lambert W Copula Analysis")
print("=" * 70)

# ==========================================================
# Load Dataset
# ==========================================================

data = load_csv("data/Temp_Precipitation.csv")

print("\nFirst Five Observations")
print("-" * 70)
print(data.head())

print("\nSummary Statistics")
print("-" * 70)
print(data.describe())

# ==========================================================
# Preprocessing
# ==========================================================

print("\nRunning Preprocessing...")
print("-" * 70)

preprocessing_summary(data)

# Remove missing observations
data = remove_missing(data)

# NOTE:
# Climate datasets may naturally contain repeated values,
# therefore duplicate observations are not removed
# automatically.
#
# Uncomment if required.
#
# data = remove_duplicates(data)

# Convert to pseudo-observations
pseudo = pseudo_observations(data)

print("\nFirst Five Pseudo-observations")
print("-" * 70)
print(pseudo.head())

print("\nValidation")
print("-" * 70)
print("Valid pseudo-observations :", validate_pseudo(pseudo))

# ==========================================================
# Empirical Copula
# ==========================================================

print("\nEmpirical Copula")
print("-" * 70)

u = pseudo.iloc[:, 0].values
v = pseudo.iloc[:, 1].values

value = empirical_copula(
    u,
    v,
    0.50,
    0.50,
)

print(f"C(0.50,0.50) = {value:.6f}")

# ==========================================================
# Empirical Surface
# ==========================================================

print("\nComputing Empirical Surface")
print("-" * 70)

x, y, Z = empirical_surface(
    u,
    v,
    grid=100,
)

print(f"Grid Size : {Z.shape}")
print(f"Minimum   : {Z.min():.6f}")
print(f"Maximum   : {Z.max():.6f}")

# ==========================================================
# Maximum Likelihood Estimation
# ==========================================================

print("\nMaximum Likelihood Estimation")
print("-" * 70)

result = fit_optimizer(
    u,
    v,
)

print(result)

theta_hat = result.theta

# ==========================================================
# Theoretical Copula Surface
# ==========================================================

print("\nComputing Theoretical Copula Surface")
print("-" * 70)

x_fit, y_fit, Z_fit = theoretical_surface(
    theta_hat,
    grid=100,
)

print(f"Grid Size : {Z_fit.shape}")
print(f"Minimum   : {Z_fit.min():.6f}")
print(f"Maximum   : {Z_fit.max():.6f}")

# ==========================================================
# Goodness-of-Fit
# ==========================================================

print("\nGoodness-of-Fit")
print("-" * 70)

RMSE = rmse(Z, Z_fit)
MAE = mae(Z, Z_fit)
MAX = max_error(Z, Z_fit)
CVM = cramer_von_mises(Z, Z_fit)
KS = kolmogorov_smirnov(Z, Z_fit)

print(f"RMSE                : {RMSE:.6f}")
print(f"MAE                 : {MAE:.6f}")
print(f"Maximum Error       : {MAX:.6f}")
print(f"Cramér-von Mises    : {CVM:.6f}")
print(f"Kolmogorov-Smirnov  : {KS:.6f}")

# ==========================================================
# Model Summary
# ==========================================================

print("\nModel Summary")
print("-" * 70)

print(f"Sample Size         : {len(u)}")
print(f"Empirical C(0.5,0.5): {value:.6f}")
print(f"RMSE                : {RMSE:.6f}")
print(f"MAE                 : {MAE:.6f}")
print(f"Maximum Error       : {MAX:.6f}")
print(f"Cramér-von Mises    : {CVM:.6f}")
print(f"Kolmogorov-Smirnov  : {KS:.6f}")

# ==========================================================
# Dependence Diagnostics
# ==========================================================

print("\nDependence Diagnostics")
print("-" * 70)

thresholds = [0.70, 0.80, 0.90]

for threshold in thresholds:

    tail_probability = conditional_tail_probability(
        u=threshold,
        v=threshold,
        theta=theta_hat,
    )

    conditional_mean = conditional_expectation(
        v=threshold,
        theta=theta_hat,
    )

    print("-" * 35)
    print(f"Threshold : {threshold:.2f}")

    print(
        f"P(U>{threshold:.2f} | V>{threshold:.2f}) : "
        f"{tail_probability:.6f}"
    )

    print(
        f"E(U | V>{threshold:.2f})                 : "
        f"{conditional_mean:.6f}"
    )

# ==========================================================
# Simulation
# ==========================================================

print("\nSimulation")
print("-" * 70)

set_seed(123)

u_sim, v_sim = simulate(
    theta_hat,
    n=1000,
)

print("First 10 Simulated Observations")
print("-" * 70)

for i in range(10):

    print(
        f"{i+1:2d}: "
        f"U = {u_sim[i]:.6f}, "
        f"V = {v_sim[i]:.6f}"
    )

print("\nSimulation Summary")
print("-" * 70)

print(f"Sample Size : {len(u_sim)}")
print(f"Mean(U)     : {u_sim.mean():.6f}")
print(f"Mean(V)     : {v_sim.mean():.6f}")
print(f"Var(U)      : {u_sim.var():.6f}")
print(f"Var(V)      : {v_sim.var():.6f}")
print(f"Corr(U,V)   : {np.corrcoef(u_sim, v_sim)[0,1]:.6f}")

# ==========================================================
# Visualization
# ==========================================================

print("\nGenerating Figures")
print("-" * 70)

raw_scatter_plot(
    data.iloc[:, 0],
    data.iloc[:, 1],
    save="figures/raw_scatter.png",
)

scatter_plot(
    u,
    v,
    save="figures/pseudo_scatter.png",
)

heat_map(
    x,
    y,
    Z,
    save="figures/empirical_heatmap.png",
)

contour_plot(
    x,
    y,
    Z,
    u,
    v,
    save="figures/empirical_contour.png",
)

surface_plot(
    x,
    y,
    Z,
    title="Empirical Copula Surface",
    save="figures/empirical_surface.png",
)

surface_plot(
    x_fit,
    y_fit,
    Z_fit,
    title="Theoretical Lambert W Copula Surface",
    save="figures/theoretical_surface.png",
)

print("\n✓ Raw data scatter plot saved")
print("✓ Pseudo-observations scatter plot saved")
print("✓ Empirical heat map saved")
print("✓ Empirical contour plot saved")
print("✓ Empirical surface saved")
print("✓ Theoretical Lambert W surface saved")

print("\nAnalysis completed successfully.")