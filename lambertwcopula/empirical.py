"""
Empirical Copula
================

Utilities for computing and visualizing
the empirical copula.
"""

import numpy as np


# ==========================================================
# Empirical Copula
# ==========================================================

def empirical_copula(u, v, x, y):
    """
    Compute the empirical copula

        C_n(x,y)

    Parameters
    ----------
    u : array-like
        Pseudo-observations.

    v : array-like
        Pseudo-observations.

    x, y : float

    Returns
    -------
    float
    """

    u = np.asarray(u)
    v = np.asarray(v)

    n = len(u)

    return np.sum((u <= x) & (v <= y)) / n


# ==========================================================
# Empirical Surface
# ==========================================================

def empirical_surface(u, v, grid=30):
    """
    Compute the empirical copula
    on a regular grid.
    """

    x = np.linspace(0, 1, grid)
    y = np.linspace(0, 1, grid)

    Z = np.zeros((grid, grid))

    for i in range(grid):
        for j in range(grid):

            Z[i, j] = empirical_copula(
                u,
                v,
                x[i],
                y[j],
            )

    return x, y, Z