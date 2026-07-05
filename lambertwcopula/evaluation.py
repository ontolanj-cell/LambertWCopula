"""
Copula Model Evaluation Framework (CMEF)
========================================

A unified framework for evaluating copula models.

Author: Jay Ontolan
"""

# ==========================================================
# Parameter Estimation
# ==========================================================

def parameter_estimation(result):

    return {

        "Theta": result.theta,

        "Std. Error": result.std_error,

        "Variance": result.variance,

        "Z Statistic": result.z_value,

        "P-value": result.p_value,

        "95% CI Lower": result.ci_lower,

        "95% CI Upper": result.ci_upper,

    }


# ==========================================================
# Local Surface Fit
# ==========================================================

def local_surface_fit(
    mse,
    rmse,
    mae,
    maximum_error,
):

    return {

        "MSE": mse,

        "RMSE": rmse,

        "MAE": mae,

        "Maximum Error": maximum_error,

    }


# ==========================================================
# Global Model Fit
# ==========================================================

def global_model_fit(
    result,
    cvm,
    ks,
):

    return {

        "Log-Likelihood": result.loglik,

        "AIC": result.aic,

        "BIC": result.bic,

        "Cramér-von Mises": cvm,

        "Kolmogorov-Smirnov": ks,

    }


# ==========================================================
# Model Stability
# ==========================================================

def model_stability(
    bootstrap,
    cv,
):

    return {

        "Bootstrap Mean": bootstrap["mean"],

        "Bootstrap Bias": bootstrap["bias"],

        "Bootstrap Variance": bootstrap["variance"],

        "Bootstrap Std. Error": bootstrap["std_error"],

        "Bootstrap CI Lower": bootstrap["ci_lower"],

        "Bootstrap CI Upper": bootstrap["ci_upper"],

        "CV Mean Theta": cv["theta_mean"],

        "CV Median Theta": cv["theta_median"],

        "CV Std. Dev.": cv["theta_sd"],

        "CV Coefficient of Variation (%)": cv["theta_cv"],

        "CV Mean Log-Likelihood": cv["loglik_mean"],

    }