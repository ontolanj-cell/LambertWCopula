"""
Report Builder
==============

Creates a unified report dictionary from the complete
AnalysisContext.

Author: Jay Ontolan
"""


# ==========================================================
# Build Report
# ==========================================================

def build_report(context):
    """
    Build a unified report from the complete analysis context.
    """

    result = context.result

    analysis = context.analysis

    bootstrap = context.bootstrap

    cv = context.cv

    winner = context.winner

    fit = analysis["fit"]

    empirical = context.empirical

    theoretical = context.theoretical

    return {

        # ==================================================
        # Parameter Estimation
        # ==================================================

        "theta": result.theta,

        "loglik": result.loglik,

        "std_error": result.std_error,

        "variance": result.variance,

        "z_value": result.z_value,

        "p_value": result.p_value,

        "ci_lower": result.ci_lower,

        "ci_upper": result.ci_upper,

        "aic": result.aic,

        "bic": result.bic,

        # ==================================================
        # Local Surface Fit
        # ==================================================

        "rmse": fit["rmse"],

        "mae": fit["mae"],

        "maximum_error": fit["maximum_error"],

        "cramer_von_mises": fit["cvm"],

        "kolmogorov_smirnov": fit["ks"],

        # ==================================================
        # Bootstrap
        # ==================================================

        "bootstrap_mean": bootstrap["mean"],

        "bootstrap_bias": bootstrap["bias"],

        "bootstrap_variance": bootstrap["variance"],

        "bootstrap_std_error": bootstrap["std_error"],

        "bootstrap_ci_lower": bootstrap["ci_lower"],

        "bootstrap_ci_upper": bootstrap["ci_upper"],

        # ==================================================
        # Cross Validation
        # ==================================================

        "cv_folds": cv["folds"],

        "cv_repeats": cv["repeats"],

        "cv_theta_mean": cv["theta_mean"],

        "cv_theta_median": cv["theta_median"],

        "cv_theta_sd": cv["theta_sd"],

        "cv_theta_cv_percent": cv["theta_cv"],

        "cv_theta_min": cv["theta_min"],

        "cv_theta_max": cv["theta_max"],

        "cv_loglik_mean": cv["loglik_mean"],

        "cv_loglik_sd": cv["loglik_sd"],

        # ==================================================
        # Model Comparison
        # ==================================================

        "best_model": winner["Model"],

        # ==================================================
        # Dataset Information
        # ==================================================

        "sample_size": len(context.u),

        "empirical_copula_0505": empirical.get("value"),

        "empirical_grid_size": empirical["surface"].shape[0],

        "theoretical_grid_size": theoretical["surface"].shape[0],

    }