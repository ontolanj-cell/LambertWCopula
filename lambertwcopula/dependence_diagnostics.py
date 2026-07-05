"""
Dependence Diagnostics
======================

Analytical dependence diagnostics for the Lambert W Copula.

Author: Jay Ontolan
"""

import numpy as np

from .psi import psi
from .closed_form import I_numeric


# ==========================================================
# Conditional Tail Probability
# ==========================================================

def conditional_tail_probability(
    u,
    v,
    theta,
):
    """
    Compute

        P(U > u | V > v)

    under the Lambert W Copula.

    Parameters
    ----------
    u : float or ndarray
        Threshold for U.

    v : float or ndarray
        Threshold for V.

    theta : float
        Dependence parameter.

    Returns
    -------
    float or ndarray
        Conditional tail probability.
    """

    u = np.asarray(u, dtype=float)
    v = np.asarray(v, dtype=float)

    return (
        1
        - u
        + theta * psi(u) * psi(v) / (1 - v)
    )


# ==========================================================
# Conditional Expectation
# ==========================================================

def conditional_expectation(
    v,
    theta,
):
    """
    Compute

        E(U | V > v)

    under the Lambert W Copula.

    Parameters
    ----------
    v : float or ndarray

    theta : float

    Returns
    -------
    float or ndarray
    """

    v = np.asarray(v, dtype=float)

    I0 = I_numeric(0)

    return (
        0.5
        + theta * I0 * psi(v) / (1 - v)
    )