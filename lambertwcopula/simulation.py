"""
Simulation Utilities
====================

Simulation methods for the Lambert W Copula.
"""

import numpy as np


# ==========================================================
# Random Seed
# ==========================================================

def set_seed(seed):
    """
    Set NumPy random seed.
    """

    np.random.seed(seed)


# ==========================================================
# Independent Uniform Sample
# ==========================================================

def simulate(theta, n):
    """
    Generate a sample.

    Version 1:
    Independent uniforms.

    Future versions will implement
    exact Lambert W copula sampling.
    """

    u = np.random.rand(n)

    v = np.random.rand(n)

    return u, v


# ==========================================================
# Alias
# ==========================================================

sample = simulate