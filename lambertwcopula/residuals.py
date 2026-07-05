"""
Residual Diagnostics
====================

Empirical minus theoretical copula.
"""

import numpy as np


def residual_surface(
    empirical,
    theoretical,
):
    """
    Residual surface.

    Returns
    -------
    Empirical - Theoretical
    """

    empirical = np.asarray(empirical)

    theoretical = np.asarray(theoretical)

    return empirical - theoretical


def residual_summary(
    residuals,
):
    """
    Summary statistics.
    """

    residuals = np.asarray(residuals)

    return {

        "minimum": residuals.min(),

        "maximum": residuals.max(),

        "mean": residuals.mean(),

        "std": residuals.std(),

    }