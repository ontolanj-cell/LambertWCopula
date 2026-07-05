"""
Lambert W Copula Package
========================

Reference implementation of the Lambert W Copula.

Author: Jay Ontolan
"""

# ==========================================================
# Constants
# ==========================================================

from .constants import (
    OMEGA,
    EPS,
    BETA,
    THETA_MIN,
    THETA_MAX,
)

# ==========================================================
# Core Functions
# ==========================================================

from .psi import psi
from .derivatives import psi_prime
from .copula import cdf
from .density import pdf

# ==========================================================
# Data Import
# ==========================================================

from .import_data import load_csv

# ==========================================================
# Preprocessing
# ==========================================================

from .preprocessing import (
    check_missing,
    remove_missing,
    remove_duplicates,
    pseudo_observations,
    validate_pseudo,
    preprocessing_summary,
)

# ==========================================================
# Empirical Copula
# ==========================================================

from .empirical import (
    empirical_copula,
    empirical_surface,
)

# ==========================================================
# Theoretical Copula
# ==========================================================

from .theoretical import (
    theoretical_surface,
)

# ==========================================================
# Goodness-of-Fit
# ==========================================================

from .goodness_of_fit import (
    residuals,
    rmse,
    mae,
    max_error,
    cramer_von_mises,
    kolmogorov_smirnov,
)

from .residuals import (
    residual_surface,
    residual_summary,
)

from .visualization_residuals import (
    residual_heatmap,
    residual_surface_plot,
)

# ==========================================================
# Statistical Inference
# ==========================================================

from .inference import (
    wald_test,
    confidence_interval,
    likelihood_ratio_test,
    score_test,
)

# ==========================================================
# Dependence Diagnostics
# ==========================================================

from .dependence_diagnostics import (
    conditional_tail_probability,
    conditional_expectation,
)

# ==========================================================
# Simulation
# ==========================================================

from .simulation import (
    set_seed,
    simulate,
    sample,
)

# ==========================================================
# Bootstrap
# ==========================================================

from .bootstrap import (
    bootstrap_theta,
    bootstrap_bias,
    bootstrap_variance,
    bootstrap_std_error,
    bootstrap_confidence_interval,
    bootstrap_summary,
)

# ==========================================================
# Cross Validation
# ==========================================================

from .cross_validation import (
    kfold_cv,
)

# ==========================================================
# Diagnostic Plots
# ==========================================================

from .diagnostic_plots import (
    histogram,
    boxplot,
)

# ==========================================================
# Model Comparison
# ==========================================================

from .comparison import (
    model_summary,
    compare_models,
    rank_models,
    best_model,
    comparison_table,
    print_comparison,
)

# ==========================================================
# Automatic Interpretation
# ==========================================================

from .interpretation import (

    interpretation_report,

)


# ==========================================================
# Report Generation
# ==========================================================

from .report import (
    save_text_report,
    save_json,
    save_csv,
)

# ==========================================================
# Visualization
# ==========================================================

from .visualization import (
    raw_scatter_plot,
    scatter_plot,
    heat_map,
    contour_plot,
    surface_plot,
)

# ==========================================================
# Moments
# ==========================================================

from .moments import (
    I,
    mixed_moment,
    covariance,
    correlation,
)

# ==========================================================
# Dependence Measures
# ==========================================================

from .dependence import (
    kendall_tau,
    spearman_rho,
    blomqvist_beta,
    relation,
)

# ==========================================================
# Closed-form Results
# ==========================================================

from .closed_form import (
    I_numeric,
    J_numeric,
    polynomial_part,
)

# ==========================================================
# Estimation Results
# ==========================================================

from .results import MLEResult

# ==========================================================
# Maximum Likelihood Estimation
# ==========================================================

from .mle import (
    ai,
    score,
    hessian,
    fisher_information,
    log_likelihood,
    aic,
    bic,
    fit_score,
    fit_optimizer,
)

from .likelihood_profile import (
    likelihood_profile,
    likelihood_plot,
)

from .html_report import generate_html


# ==========================================================
# Analysis
# ==========================================================

from .analysis import (

    goodness_of_fit_analysis,

    residual_analysis,

    analyze_model,

)


# ==========================================================
# Report Builder
# ==========================================================

from .report_builder import (

    build_report,

)


# ==========================================================
# Figure Manager
# ==========================================================

from .figure_manager import (

    generate_likelihood_profile,

    generate_main_figures,

    generate_bootstrap_figures,

    generate_cv_figures,

    generate_all_figures,

)


# ==========================================================
# Context
# ==========================================================

from .context import AnalysisContext


# ==========================================================
# Benchmark Copulas
# ==========================================================

from .benchmark import (
    fit_gaussian,
    fit_all_copulas,
    best_model,
    print_comparison,
)

# ==========================================================
# Copula Model Evaluation Framework
# ==========================================================

from .evaluation import (

    parameter_estimation,

    local_surface_fit,

    global_model_fit,

    model_stability,

)


# ==========================================================
# Copula Model Evaluation Framework
# ==========================================================

from .cmef import (
    dataset_summary,
    parameter_estimation,
    local_surface_fit,
    global_model_fit,
    model_stability,
    model_comparison,
    automatic_interpretation,
)

from .pipeline import AnalysisPipeline

# ==========================================================
# Package Information
# ==========================================================

__version__ = "0.1.0"

__author__ = "Jay Ontolan"

# ==========================================================
# Public API
# ==========================================================

__all__ = [

    # Constants
    "OMEGA",
    "EPS",
    "BETA",
    "THETA_MIN",
    "THETA_MAX",

    # Core
    "psi",
    "psi_prime",
    "cdf",
    "pdf",

    # Data Import
    "load_csv",

    # Preprocessing
    "check_missing",
    "remove_missing",
    "remove_duplicates",
    "pseudo_observations",
    "validate_pseudo",
    "preprocessing_summary",

    # Empirical Copula
    "empirical_copula",
    "empirical_surface",

    # Theoretical Copula
    "theoretical_surface",

    # Goodness-of-Fit
    "residuals",
    "rmse",
    "mae",
    "max_error",
    "cramer_von_mises",
    "kolmogorov_smirnov",
    "residual_surface",
    "residual_summary",

    "residual_heatmap",
    "residual_surface_plot",

    # Dependence Diagnostics
    "conditional_tail_probability",
    "conditional_expectation",

    # Statistical Inference
    "wald_test",
    "confidence_interval",
    "likelihood_ratio_test",
    "score_test",

    # Simulation
    "set_seed",
    "simulate",
    "sample",

    # Bootstrap
    "bootstrap_theta",
    "bootstrap_bias",
    "bootstrap_variance",
    "bootstrap_std_error",
    "bootstrap_confidence_interval",
    "bootstrap_summary",

    "kfold_cv",


    "histogram",
    "boxplot",

    # Model Comparison
    "model_summary",
    "compare_models",
    "rank_models",
    "best_model",
    "comparison_table",
    "print_comparison",

    "interpretation_report",

    # Report Generation
    "save_text_report",
    "save_json",
    "save_csv",

    # Visualization
    "raw_scatter_plot",
    "scatter_plot",
    "heat_map",
    "contour_plot",
    "surface_plot",

    # Moments
    "I",
    "mixed_moment",
    "covariance",
    "correlation",

    # Dependence
    "kendall_tau",
    "spearman_rho",
    "blomqvist_beta",
    "relation",

    # Closed-form
    "I_numeric",
    "J_numeric",
    "polynomial_part",

    # Bencmark Copulas
    "fit_gaussian",
    "fit_all_copulas",
    "best_model",
    "print_comparison",

    "parameter_estimation",
    "local_surface_fit",
    "global_model_fit",
    "model_stability",

    # Estimation
    "likelihood_profile",
    "likelihood_plot",
    "MLEResult",
    "ai",
    "score",
    "hessian",
    "fisher_information",
    "log_likelihood",
    "aic",
    "bic",
    "fit_score",
    "fit_optimizer",
    "generate_html",

    "dataset_summary",
    "parameter_estimation",
    "local_surface_fit",
    "global_model_fit",
    "model_stability",
    "model_comparison",
    "automatic_interpretation",

    "goodness_of_fit_analysis",
    "residual_analysis",
    "analyze_model",

    "build_report",

    "generate_likelihood_profile",
    "generate_main_figures",
    "generate_bootstrap_figures",
    "generate_cv_figures",
    "generate_all_figures",

    "AnalysisContext",

    "AnalysisPipeline",
]