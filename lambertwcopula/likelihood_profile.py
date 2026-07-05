"""
Likelihood Profile
==================

Profile log-likelihood for the Lambert W Copula.
"""

import numpy as np
import matplotlib.pyplot as plt

from .mle import log_likelihood
from .constants import THETA_MIN, THETA_MAX


def likelihood_profile(
    u,
    v,
    n_points=200,
):
    """
    Compute the profile log-likelihood.

    Returns
    -------
    theta_grid
    loglikelihood
    """

    theta = np.linspace(
        THETA_MIN,
        THETA_MAX,
        n_points,
    )

    loglik = np.array(
        [
            log_likelihood(t, u, v)
            for t in theta
        ]
    )

    return theta, loglik


def likelihood_plot(
    theta,
    loglik,
    theta_hat=None,
    save=None,
):
    """
    Plot the likelihood profile.
    """

    plt.figure(figsize=(8, 5))

    plt.plot(
        theta,
        loglik,
        linewidth=2,
        label="Log-Likelihood",
    )

    if theta_hat is not None:

        plt.axvline(
            theta_hat,
            color="red",
            linestyle="--",
            linewidth=2,
            label=f"MLE = {theta_hat:.3f}",
        )

    plt.xlabel(r"$\theta$")
    plt.ylabel("Log-Likelihood")
    plt.title("Likelihood Profile")
    plt.grid(alpha=0.30)
    plt.legend()

    if save is not None:
        plt.savefig(
            save,
            dpi=300,
            bbox_inches="tight",
        )

    plt.close()