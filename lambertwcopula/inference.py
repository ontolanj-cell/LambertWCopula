"""
Statistical Inference
Lambert W Copula
"""

import numpy as np
from scipy.stats import norm


# ==========================================================
# Wald Test
# ==========================================================

def wald_test(theta, std_error):
    """
    Wald z-test for H0: theta = 0
    """

    z = theta / std_error

    p = 2 * (1 - norm.cdf(abs(z)))

    return z, p


# ==========================================================
# Confidence Interval
# ==========================================================

def confidence_interval(
    theta,
    std_error,
    alpha=0.05,
):
    """
    Two-sided confidence interval.
    """

    z = norm.ppf(1 - alpha / 2)

    lower = theta - z * std_error

    upper = theta + z * std_error

    return lower, upper


# ==========================================================
# Likelihood Ratio Test
# ==========================================================

def likelihood_ratio_test(
    loglik_null,
    loglik_alt,
):
    """
    Likelihood Ratio Test.
    """

    LR = 2 * (loglik_alt - loglik_null)

    p = 1 - norm.cdf(np.sqrt(LR))

    return LR, p


# ==========================================================
# Score Test
# ==========================================================

def score_test(
    score,
    information,
):
    """
    Rao Score Test.
    """

    statistic = score ** 2 / information

    p = 1 - norm.cdf(np.sqrt(statistic))

    return statistic, p