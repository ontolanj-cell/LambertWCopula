"""
Closed-form analytical formulas for the Lambert W Copula.

Implements the theoretical expressions derived in the dissertation.
"""

import numpy as np
from scipy.special import gamma
from scipy.integrate import quad

from .constants import OMEGA
from .psi import psi


def I_numeric(n):
    """
    Numerical evaluation of

        I_n = ∫_0^1 u^n Ψ(u) du
    """

    value, _ = quad(
        lambda u: (u ** n) * psi(u),
        0,
        1
    )

    return value


def polynomial_part(n):
    """
    Polynomial component

    Ω/(n+3) - Ω/(n+2)
    """

    return OMEGA / (n + 3) - OMEGA / (n + 2)


def J_numeric(n):
    """
    Numerical value of

        J_n

    obtained by subtracting the polynomial part.
    """

    return I_numeric(n) - polynomial_part(n)