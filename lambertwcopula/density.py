"""
Lambert W copula density.
"""

from .derivatives import psi_prime


def pdf(u, v, theta):
    """
    c(u,v)=1+theta Psi'(u)Psi'(v)
    """

    return (
        1.0
        +
        theta*psi_prime(u)*psi_prime(v)
    )