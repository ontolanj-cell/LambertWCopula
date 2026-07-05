"""
Lambert W copula CDF.
"""

from .psi import psi


def cdf(u, v, theta):
    """
    C(u,v)=uv+theta*Psi(u)Psi(v)
    """

    return (
        u*v
        +
        theta*psi(u)*psi(v)
    )