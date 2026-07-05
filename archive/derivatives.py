from scipy.special import lambertw
import numpy as np

OMEGA = np.real(lambertw(1))


def psi_prime(u):

    u = np.asarray(u)

    W = np.real(lambertw(u))

    return (
        (1 - 2*u)*(W - OMEGA)
        +
        (1-u)*W/(1+W)
    )