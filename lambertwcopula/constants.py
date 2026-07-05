"""
Constants for the Lambert W Copula package.
"""

import numpy as np
from scipy.special import lambertw

OMEGA = np.real(lambertw(1.0))

EPS = 1e-12

BETA = 0.14816

THETA_MIN = -1.0 / (OMEGA ** 2)
THETA_MAX = 1.0 / (OMEGA * BETA)