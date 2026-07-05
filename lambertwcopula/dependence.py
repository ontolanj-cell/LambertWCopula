"""
Dependence measures for the Lambert W Copula
"""

from .moments import I


def covariance(theta):
    """
    Cov(U,V)
    """

    return theta * I(0)**2


def correlation(theta):
    """
    Pearson correlation
    """

    return 12 * covariance(theta)


def kendall_tau(theta):
    """
    Kendall's tau

    τ = 4 θ I0²
    """

    return 4 * theta * I(0)**2


def spearman_rho(theta):
    """
    Spearman's rho

    ρ = 12 θ I0²
    """

    return 12 * theta * I(0)**2


def blomqvist_beta(theta, psi_half):
    """
    β = θ ψ(1/2)²
    """

    return theta * psi_half**2


def relation(theta):
    """
    Verify ρ = 3τ
    """

    tau = kendall_tau(theta)

    rho = spearman_rho(theta)

    return rho / tau