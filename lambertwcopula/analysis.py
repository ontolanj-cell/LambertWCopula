"""
Analysis utilities for Lambert W Copula.

Author: Jay Ontolan
"""

from .goodness_of_fit import (
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


# ==========================================================
# Goodness-of-Fit Analysis
# ==========================================================

def goodness_of_fit_analysis(
    empirical,
    theoretical,
):
    """
    Compute all goodness-of-fit measures.
    """

    return {

        "rmse": rmse(
            empirical,
            theoretical,
        ),

        "mae": mae(
            empirical,
            theoretical,
        ),

        "maximum_error": max_error(
            empirical,
            theoretical,
        ),

        "cvm": cramer_von_mises(
            empirical,
            theoretical,
        ),

        "ks": kolmogorov_smirnov(
            empirical,
            theoretical,
        ),

    }


# ==========================================================
# Residual Analysis
# ==========================================================

def residual_analysis(
    empirical,
    theoretical,
):
    """
    Compute residual diagnostics.
    """

    R = residual_surface(
        empirical,
        theoretical,
    )

    stats = residual_summary(R)

    return {

        "surface": R,

        "summary": stats,

    }


# ==========================================================
# Complete Analysis
# ==========================================================

def analyze_model(
    empirical,
    theoretical,
):
    """
    Perform the complete model analysis.
    """

    fit = goodness_of_fit_analysis(
        empirical,
        theoretical,
    )

    residuals = residual_analysis(
        empirical,
        theoretical,
    )

    return {

        "fit": fit,

        "residuals": residuals,

    }