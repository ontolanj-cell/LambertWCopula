"""
Lambert W generating function.
"""

import numpy as np
from scipy.special import lambertw

from .constants import OMEGA


def psi(u):
    """
    Psi(u)=u(1-u)(W(u)-Omega)
    """

    u = np.asarray(u, dtype=float)

    W = np.real(lambertw(u))

    return u * (1.0 - u) * (W - OMEGA)