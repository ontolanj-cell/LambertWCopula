"""
Maximum Likelihood Estimation
Lambert W Copula
"""

import numpy as np
from scipy.optimize import root_scalar
from scipy.optimize import minimize_scalar
from scipy.stats import norm

from .constants import THETA_MIN
from .constants import THETA_MAX

from .density import pdf
from .derivatives import psi_prime

from .results import MLEResult


# ==========================================================
# Auxiliary quantity
# a_i = Psi'(u_i) Psi'(v_i)
# ==========================================================

def ai(u, v):
    """
    Compute

        a_i = Psi'(u_i) Psi'(v_i)
    """

    u = np.asarray(u, dtype=float)
    v = np.asarray(v, dtype=float)

    return psi_prime(u) * psi_prime(v)


# ==========================================================
# Log Likelihood
# ==========================================================

def log_likelihood(theta, u, v):
    """
    Evaluate

        l(theta)
    """

    c = pdf(u, v, theta)

    if np.any(c <= 0):
        return -np.inf

    return np.sum(np.log(c))


# ==========================================================
# Score Function
# ==========================================================

def score(theta, u, v):
    """
    Score equation

        dl(theta)/dtheta
    """

    A = ai(u, v)

    return np.sum(
        A / (1 + theta * A)
    )


# ==========================================================
# Observed Information
# ==========================================================

def hessian(theta, u, v):
    """
    Second derivative

        d²l(theta)/dtheta²
    """

    A = ai(u, v)

    return -np.sum(
        (A ** 2) /
        (1 + theta * A) ** 2
    )


# ==========================================================
# Fisher Information
# ==========================================================

def fisher_information(theta, u, v):
    """
    Observed Fisher Information
    """

    return -hessian(theta, u, v)


# ==========================================================
# AIC
# ==========================================================

def aic(loglik, k=1):

    return 2 * k - 2 * loglik


# ==========================================================
# BIC
# ==========================================================

def bic(loglik, n, k=1):

    return np.log(n) * k - 2 * loglik


# ==========================================================
# Dissertation Estimator
# ==========================================================

def fit_score(u, v):
    """
    Estimate theta using the score equation.
    """

    u = np.asarray(u)
    v = np.asarray(v)

    n = len(u)

    fmin = score(THETA_MIN, u, v)
    fmax = score(THETA_MAX, u, v)

    if fmin * fmax < 0:

        solution = root_scalar(
            score,
            args=(u, v),
            bracket=[THETA_MIN, THETA_MAX],
            method="brentq",
        )

        theta = solution.root

        success = solution.converged

    else:

        theta = 0.0

        success = False

    loglik = log_likelihood(theta, u, v)

    info = fisher_information(theta, u, v)

    if info > 0:

        variance = 1 / info

        std_error = np.sqrt(variance)

        z_value = theta / std_error

        p_value = 2 * (1 - norm.cdf(abs(z_value)))

        ci_lower = theta - 1.96 * std_error

        ci_upper = theta + 1.96 * std_error

    else:

        variance = None

        std_error = None

        z_value = None

        p_value = None

        ci_lower = None

        ci_upper = None

    return MLEResult(

        theta=theta,

        loglik=loglik,

        method="Score Equation",

        success=success,

        iterations=None,

        aic=aic(loglik),

        bic=bic(loglik, n),

        std_error=std_error,

        variance=variance,

        z_value=z_value,

        p_value=p_value,

        ci_lower=ci_lower,

        ci_upper=ci_upper,
    )


# ==========================================================
# Numerical Optimizer
# ==========================================================

def fit_optimizer(u, v):
    """
    Independent numerical verification.
    """

    u = np.asarray(u)
    v = np.asarray(v)

    n = len(u)

    result = minimize_scalar(

        lambda t: -log_likelihood(t, u, v),

        bounds=(THETA_MIN, THETA_MAX),

        method="bounded",
    )

    theta = result.x

    loglik = -result.fun

    info = fisher_information(theta, u, v)

    if info > 0:

        variance = 1 / info

        std_error = np.sqrt(variance)

        z_value = theta / std_error

        p_value = 2 * (1 - norm.cdf(abs(z_value)))

        ci_lower = theta - 1.96 * std_error

        ci_upper = theta + 1.96 * std_error

    else:

        variance = None

        std_error = None

        z_value = None

        p_value = None

        ci_lower = None

        ci_upper = None

    return MLEResult(

        theta=theta,

        loglik=loglik,

        method="Optimizer",

        success=result.success,

        iterations=result.nfev,

        aic=aic(loglik),

        bic=bic(loglik, n),

        std_error=std_error,

        variance=variance,

        z_value=z_value,

        p_value=p_value,

        ci_lower=ci_lower,

        ci_upper=ci_upper,
    )