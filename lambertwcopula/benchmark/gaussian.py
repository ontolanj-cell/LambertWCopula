"""
Gaussian Copula
"""

import numpy as np

from scipy.stats import norm
from scipy.stats import multivariate_normal

from scipy.optimize import minimize_scalar


def gaussian_loglik(rho, u, v):

    if abs(rho) >= 0.999:
        return -np.inf

    x = norm.ppf(u)
    y = norm.ppf(v)

    cov = np.array([
        [1, rho],
        [rho, 1],
    ])

    mvn = multivariate_normal(
        mean=[0, 0],
        cov=cov,
    )

    log_joint = mvn.logpdf(
        np.column_stack([x, y])
    )

    log_margin = (
        norm.logpdf(x)
        +
        norm.logpdf(y)
    )

    return np.sum(
        log_joint
        -
        log_margin
    )


def fit_gaussian(u, v):

    result = minimize_scalar(

        lambda r: -gaussian_loglik(
            r,
            u,
            v,
        ),

        bounds=(-0.95, 0.95),

        method="bounded",
    )

    rho = result.x

    loglik = -result.fun

    n = len(u)

    return {

        "Model": "Gaussian",

        "Theta": rho,

        "LogLik": loglik,

        "AIC": 2 - 2 * loglik,

        "BIC": np.log(n) - 2 * loglik,

    }