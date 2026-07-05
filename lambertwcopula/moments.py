"""
Moments for the Lambert W Copula

Implements:

I_n = ∫ u^n Ψ(u) du

using numerical integration.

Future versions will include the closed-form
representation involving incomplete gamma functions.
"""

import numpy as np

from scipy.integrate import quad

from .psi import psi


def I(n):
    """
    Compute

        I_n = ∫_0^1 u^n Ψ(u) du

    Parameters
    ----------
    n : int

    Returns
    -------
    float
    """

    value, error = quad(

        lambda u: (u**n) * psi(u),

        0,

        1

    )

    return value


def mixed_moment(i, j, theta):
    """
    E(U^i V^j)

    using

    E(U^iV^j)

    =1/((i+1)(j+1))

    +θijI_(i−1)I_(j−1)
    """

    return (

        1 / ((i + 1) * (j + 1))

        +

        theta

        * i

        * j

        * I(i - 1)

        * I(j - 1)

    )


def covariance(theta):
    """
    Cov(U,V)
    """

    I0 = I(0)

    return theta * I0**2


def correlation(theta):
    """
    Pearson correlation
    """

    return 12 * covariance(theta)