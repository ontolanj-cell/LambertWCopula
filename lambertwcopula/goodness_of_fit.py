"""
Goodness-of-Fit Statistics
==========================

Lambert W Copula
"""

import numpy as np


# ==========================================================
# Residual Surface
# ==========================================================

def residuals(empirical, theoretical):
    """
    Residual surface.
    """

    return empirical - theoretical


# ==========================================================
# Root Mean Squared Error
# ==========================================================

def rmse(empirical, theoretical):
    """
    Root Mean Squared Error.
    """

    empirical = np.asarray(empirical)
    theoretical = np.asarray(theoretical)

    return np.sqrt(
        np.mean(
            (empirical - theoretical) ** 2
        )
    )


# ==========================================================
# Mean Absolute Error
# ==========================================================

def mae(empirical, theoretical):
    """
    Mean Absolute Error.
    """

    empirical = np.asarray(empirical)
    theoretical = np.asarray(theoretical)

    return np.mean(
        np.abs(empirical - theoretical)
    )


# ==========================================================
# Maximum Absolute Error
# ==========================================================

def max_error(empirical, theoretical):
    """
    Maximum Absolute Error.
    """

    empirical = np.asarray(empirical)
    theoretical = np.asarray(theoretical)

    return np.max(
        np.abs(empirical - theoretical)
    )


# ==========================================================
# Cramér-von Mises Statistic
# ==========================================================

def cramer_von_mises(empirical, theoretical):
    """
    Cramér-von Mises statistic.
    """

    empirical = np.asarray(empirical)
    theoretical = np.asarray(theoretical)

    return np.mean(
        (empirical - theoretical) ** 2
    )


# ==========================================================
# Kolmogorov-Smirnov Statistic
# ==========================================================

def kolmogorov_smirnov(empirical, theoretical):
    """
    Kolmogorov-Smirnov statistic.
    """

    empirical = np.asarray(empirical)
    theoretical = np.asarray(theoretical)

    return np.max(
        np.abs(empirical - theoretical)
    )