from scipy.special import lambertw
import numpy as np

OMEGA = np.real(lambertw(1))


def psi(u):

    u = np.asarray(u, dtype=float)

    return (
        u
        * (1 - u)
        * (np.real(lambertw(u)) - OMEGA)
    )