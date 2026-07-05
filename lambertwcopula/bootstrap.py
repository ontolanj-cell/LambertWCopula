"""
Bootstrap Inference
Lambert W Copula
"""

import numpy as np

from .mle import fit_optimizer


# ==========================================================
# Bootstrap Estimates
# ==========================================================

def bootstrap_theta(
    u,
    v,
    B=1000,
    random_state=None,
):
    """
    Bootstrap estimates of theta.
    """

    rng = np.random.default_rng(random_state)

    u = np.asarray(u)
    v = np.asarray(v)

    n = len(u)

    estimates = np.empty(B)

    for b in range(B):

        idx = rng.integers(
            0,
            n,
            n,
        )

        result = fit_optimizer(
            u[idx],
            v[idx],
        )

        estimates[b] = result.theta

    return estimates


# ==========================================================
# Bootstrap Bias
# ==========================================================

def bootstrap_bias(
    estimates,
    theta_hat,
):
    """
    Bootstrap bias.
    """

    estimates = np.asarray(estimates)

    return estimates.mean() - theta_hat


# ==========================================================
# Bootstrap Variance
# ==========================================================

def bootstrap_variance(
    estimates,
):
    """
    Bootstrap variance.
    """

    estimates = np.asarray(estimates)

    return estimates.var(
        ddof=1,
    )


# ==========================================================
# Bootstrap Standard Error
# ==========================================================

def bootstrap_std_error(
    estimates,
):
    """
    Bootstrap standard error.
    """

    return np.sqrt(
        bootstrap_variance(
            estimates,
        )
    )


# ==========================================================
# Percentile Confidence Interval
# ==========================================================

def bootstrap_confidence_interval(
    estimates,
    alpha=0.05,
):
    """
    Percentile bootstrap confidence interval.
    """

    lower = np.percentile(
        estimates,
        100 * alpha / 2,
    )

    upper = np.percentile(
        estimates,
        100 * (1 - alpha / 2),
    )

    return lower, upper


# ==========================================================
# Summary
# ==========================================================

def bootstrap_summary(
    estimates,
    theta_hat,
):
    """
    Complete bootstrap summary.
    """

    bias = bootstrap_bias(
        estimates,
        theta_hat,
    )

    variance = bootstrap_variance(
        estimates,
    )

    std_error = np.sqrt(
        variance,
    )

    ci = bootstrap_confidence_interval(
        estimates,
    )

    return {

        "mean": estimates.mean(),

        "bias": bias,

        "variance": variance,

        "std_error": std_error,

        "ci_lower": ci[0],

        "ci_upper": ci[1],

    }