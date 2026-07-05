"""
Theoretical Lambert W Copula
============================
"""

import numpy as np

from .copula import cdf


# ==========================================================
# Theoretical Surface
# ==========================================================

def theoretical_surface(theta, grid=100):
    """
    Compute the theoretical Lambert W copula surface.
    """

    x = np.linspace(0, 1, grid)
    y = np.linspace(0, 1, grid)

    Z = np.zeros((grid, grid))

    for i, u in enumerate(x):
        for j, v in enumerate(y):
            Z[j, i] = cdf(u, v, theta)

    return x, y, Z