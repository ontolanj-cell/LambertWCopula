"""
Repeated K-Fold Cross Validation
Lambert W Copula
"""

import numpy as np

from .mle import fit_optimizer


# ==========================================================
# Repeated K-Fold Cross Validation
# ==========================================================

def kfold_cv(
    u,
    v,
    folds=5,
    repeats=20,
    random_state=123,
):
    """
    Repeated K-Fold Cross Validation.

    Parameters
    ----------
    folds : int
        Number of folds.

    repeats : int
        Number of repetitions.

    Returns
    -------
    dict
    """

    rng = np.random.default_rng(random_state)

    u = np.asarray(u)
    v = np.asarray(v)

    n = len(u)

    theta_values = []
    loglik_values = []

    for _ in range(repeats):

        indices = rng.permutation(n)

        splits = np.array_split(indices, folds)

        for test in splits:

            train = np.setdiff1d(indices, test)

            result = fit_optimizer(
                u[train],
                v[train],
            )

            theta_values.append(result.theta)
            loglik_values.append(result.loglik)

    theta_values = np.asarray(theta_values)
    loglik_values = np.asarray(loglik_values)

    return {

        "folds": folds,

        "repeats": repeats,

        "theta_mean": theta_values.mean(),

        "theta_median": np.median(theta_values),

        "theta_sd": theta_values.std(ddof=1),

        "theta_min": theta_values.min(),

        "theta_max": theta_values.max(),

        "theta_cv": (
            theta_values.std(ddof=1)
            / theta_values.mean()
            * 100
        ),

        "loglik_mean": loglik_values.mean(),

        "loglik_sd": loglik_values.std(ddof=1),

        "theta_values": theta_values,

        "loglik_values": loglik_values,

    }