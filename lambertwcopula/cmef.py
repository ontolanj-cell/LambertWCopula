"""
Copula Model Evaluation Framework (CMEF)

Author: Jay Ontolan
"""


from .benchmark import print_comparison

# ==========================================================
# Dataset Summary
# ==========================================================

def dataset_summary(n):

    print("\nI. Dataset Summary")
    print("-" * 70)

    print(f"Sample Size : {n}")


# ==========================================================
# Parameter Estimation
# ==========================================================

def parameter_estimation(result):

    print("\nII. Parameter Estimation")
    print("-" * 70)

    print(f"Theta             : {result.theta:.6f}")
    print(f"Std. Error        : {result.std_error:.6f}")
    print(f"Variance          : {result.variance:.6f}")
    print(f"z Statistic       : {result.z_value:.6f}")
    print(f"p-value           : {result.p_value:.6f}")
    print(
        f"95% CI            : "
        f"({result.ci_lower:.6f}, "
        f"{result.ci_upper:.6f})"
    )


# ==========================================================
# Local Surface Fit
# ==========================================================

def local_surface_fit(
    rmse,
    mae,
    maximum_error,
):

    print("\nIII. Local Surface Fit")
    print("-" * 70)

    print(f"MSE               : {rmse**2:.6f}")
    print(f"RMSE              : {rmse:.6f}")
    print(f"MAE               : {mae:.6f}")
    print(f"Maximum Error     : {maximum_error:.6f}")


# ==========================================================
# Global Model Fit
# ==========================================================

def global_model_fit(
    result,
    cvm,
    ks,
):

    print("\nIV. Global Model Fit")
    print("-" * 70)

    print(f"Log-Likelihood    : {result.loglik:.6f}")
    print(f"AIC               : {result.aic:.6f}")
    print(f"BIC               : {result.bic:.6f}")
    print(f"Cramér-von Mises  : {cvm:.6f}")
    print(f"Kolmogorov-Smirnov: {ks:.6f}")


# ==========================================================
# Model Stability
# ==========================================================

def model_stability(
    summary,
    cv,
):

    print("\nV. Model Stability")
    print("-" * 70)

    print(f"Bootstrap Mean    : {summary['mean']:.6f}")
    print(f"Bootstrap Bias    : {summary['bias']:.6f}")
    print(f"Bootstrap Std Err : {summary['std_error']:.6f}")
    print(f"CV Mean Theta     : {cv['theta_mean']:.6f}")
    print(f"CV Theta SD       : {cv['theta_sd']:.6f}")
    print(f"CV Coef. Var (%)  : {cv['theta_cv']:.2f}")


# ==========================================================
# Model Comparison
# ==========================================================

def model_comparison(
    models,
    winner,
):

    print("\nVI. Model Comparison")
    print("-" * 70)

    print_comparison(models)

    print("\nPreferred Model")
    print("-" * 70)

    print(winner["Model"])


# ==========================================================
# Automatic Interpretation
# ==========================================================

def automatic_interpretation(report):

    print("\nVII. Automatic Interpretation")
    print("-" * 70)

    for sentence in report:

        print("•", sentence)