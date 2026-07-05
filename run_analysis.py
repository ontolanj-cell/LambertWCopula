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
# Initialize Pipeline
# ==========================================================

pipeline = AnalysisPipeline()

context = pipeline.ctx

# ==========================================================
# Load Dataset
# ==========================================================

data = pipeline.load_data(
    "data/Temp_Precipitation.csv"
)

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


context.pseudo = pseudo

context.u = u

context.v = v

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

context.empirical = {

    "x": x,

    "y": y,

    "surface": Z,

    "value": value,

}

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

context.result = result
print(result)

print("\nParameter Significance")
print("-" * 70)

print(f"z Statistic : {result.z_value:.6f}")
print(f"p-value     : {result.p_value:.6f}")
print(f"95% CI      : ({result.ci_lower:.6f}, {result.ci_upper:.6f})")

theta_hat = result.theta

# ==========================================================
# Likelihood Profile
# ==========================================================

print("\nLikelihood Profile")
print("-" * 70)

theta_grid, loglik_grid = likelihood_profile(
    u,
    v,
)

likelihood_plot(
    theta_grid,
    loglik_grid,
    theta_hat=theta_hat,
    save="figures/likelihood_profile.png",
)

print("✓ Likelihood profile generated")


# ==========================================================
# Theoretical Copula Surface
# ==========================================================

print("\nComputing Theoretical Copula Surface")
print("-" * 70)

x_fit, y_fit, Z_fit = theoretical_surface(
    theta_hat,
    grid=100,
)

context.theoretical = {

    "x": x_fit,

    "y": y_fit,

    "surface": Z_fit,

}

print(f"Grid Size : {Z_fit.shape}")
print(f"Minimum   : {Z_fit.min():.6f}")
print(f"Maximum   : {Z_fit.max():.6f}")

# ==========================================================
# Goodness-of-Fit
# ==========================================================

print("\nGoodness-of-Fit")
print("-" * 70)

analysis = analyze_model(
    Z,
    Z_fit,
)

context.analysis = analysis

fit = analysis["fit"]

R = analysis["residuals"]["surface"]

stats = analysis["residuals"]["summary"]

print(f"RMSE                : {fit['rmse']:.6f}")
print(f"MAE                 : {fit['mae']:.6f}")
print(f"Maximum Error       : {fit['maximum_error']:.6f}")
print(f"Cramér-von Mises    : {fit['cvm']:.6f}")
print(f"Kolmogorov-Smirnov  : {fit['ks']:.6f}")

# ==========================================================
# Residual Diagnostics
# ==========================================================

print("\nResidual Diagnostics")
print("-" * 70)


print(f"Minimum Residual : {stats['minimum']:.6f}")
print(f"Maximum Residual : {stats['maximum']:.6f}")
print(f"Mean Residual    : {stats['mean']:.6f}")
print(f"Std. Residual    : {stats['std']:.6f}")


# ==========================================================
# Model Summary
# ==========================================================

print("\nModel Summary")
print("-" * 70)

print(f"Sample Size         : {len(context.u)}")
print(f"Empirical C(0.5,0.5): {context.empirical['value']:.6f}")
print(f"RMSE                : {fit['rmse']:.6f}")
print(f"MAE                 : {fit['mae']:.6f}")
print(f"Maximum Error       : {fit['maximum_error']:.6f}")
print(f"Cramér-von Mises    : {fit['cvm']:.6f}")
print(f"Kolmogorov-Smirnov  : {fit['ks']:.6f}")

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

context.simulation = {

    "u": u_sim,

    "v": v_sim,

}

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
# Bootstrap
# ==========================================================

print("\nBootstrap Inference")
print("-" * 70)

estimates = bootstrap_theta(
    u,
    v,
    B=500,
    random_state=123,
)

summary = bootstrap_summary(
    estimates,
    theta_hat,
)

context.estimates = estimates

context.bootstrap = summary


print(f"Mean           : {summary['mean']:.6f}")
print(f"Bias           : {summary['bias']:.6f}")
print(f"Variance       : {summary['variance']:.6f}")
print(f"Std. Error     : {summary['std_error']:.6f}")
print(f"95% CI Lower   : {summary['ci_lower']:.6f}")
print(f"95% CI Upper   : {summary['ci_upper']:.6f}")


# ==========================================================
# Cross Validation
# ==========================================================

print("\nCross Validation")
print("-" * 70)

cv = kfold_cv(
    u,
    v,
    folds=5,
    repeats=20,
)

context.cv = cv

print(f"Folds               : {cv['folds']}")
print(f"Repeats             : {cv['repeats']}")

print(f"Mean Theta          : {cv['theta_mean']:.6f}")
print(f"Median Theta        : {cv['theta_median']:.6f}")
print(f"Std. Dev.           : {cv['theta_sd']:.6f}")
print(f"Coefficient of Var. : {cv['theta_cv']:.2f}%")
print(f"Minimum Theta       : {cv['theta_min']:.6f}")
print(f"Maximum Theta       : {cv['theta_max']:.6f}")

print(f"Mean LogLik         : {cv['loglik_mean']:.6f}")
print(f"LogLik Std. Dev.    : {cv['loglik_sd']:.6f}")

# ==========================================================
# Model Comparison
# ==========================================================

print("\nModel Comparison")
print("-" * 70)

lambert = {

    "Model": "Lambert W",

    "Theta": result.theta,

    "LogLik": result.loglik,

    "AIC": result.aic,

    "BIC": result.bic,

}

models = fit_all_copulas(
    u,
    v,
    lambert,
)

context.models = models

print_comparison(models)

winner = best_model(models)

context.winner = winner

print("\nBest Model")
print("-" * 70)

print(winner["Model"])

# ==========================================================
# Automatic Interpretation
# ==========================================================

print("\nAutomatic Interpretation")
print("-" * 70)

context.interpretation = interpretation_report(
    result,
    fit["rmse"],
    fit["mae"],
    summary,
    cv,
)

for sentence in context.interpretation:

    print("•", sentence)

# ==========================================================
# Export Reports
# ==========================================================

print("\nSaving Reports")
print("-" * 70)

results = build_report(context)

save_text_report(
    results,
    filename="reports/results.txt",
)

save_json(
    results,
    filename="reports/results.json",
)

save_csv(
    results,
    filename="reports/results.csv",
)

print("✓ Text report saved")
print("✓ JSON report saved")
print("✓ CSV report saved")
generate_all_figures(context)
generate_html(

    results,

    figures=[

        "figures/raw_scatter.png",

        "figures/pseudo_scatter.png",

        "figures/empirical_heatmap.png",

        "figures/empirical_contour.png",

        "figures/empirical_surface.png",

        "figures/theoretical_surface.png",

        "figures/bootstrap_histogram.png",

        "figures/bootstrap_boxplot.png",

        "figures/cv_histogram.png",

        "figures/cv_boxplot.png",

        "figures/likelihood_profile.png",

        "figures/residual_heatmap.png",

        "figures/residual_surface.png",

    ],

    filename="reports/report.html",

)

print("✓ HTML report saved")

# ==========================================================
# Visualization
# ==========================================================

print("\n" + "=" * 70)
print("Lambert W Copula analysis completed successfully.")
print("Reports saved to : reports/")
print("Figures saved to : figures/")
print("=" * 70)