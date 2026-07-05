"""
First derivative of the Lambert W generating function.
"""

import numpy as np
from scipy.special import lambertw

from .constants import OMEGA


def psi_prime(u):
    """
    Psi'(u)
    """

    u = np.asarray(u, dtype=float)

    W = np.real(lambertw(u))

    return (
        (1.0 - 2.0*u)*(W - OMEGA)
        +
        ((1.0-u)*W)/(1.0+W)
    )