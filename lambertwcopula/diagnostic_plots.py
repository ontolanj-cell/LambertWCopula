"""
Diagnostic plots for Lambert W Copula.
"""

from pathlib import Path

import matplotlib.pyplot as plt


# ==========================================================
# Histogram
# ==========================================================

def histogram(
    values,
    title,
    xlabel,
    save=None,
):
    """
    Histogram of parameter estimates.
    """

    plt.figure(figsize=(7, 5))

    plt.hist(
        values,
        bins=20,
        edgecolor="black",
    )

    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel("Frequency")

    plt.tight_layout()

    if save is not None:

        Path(save).parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        plt.savefig(
            save,
            dpi=300,
            bbox_inches="tight",
        )

    plt.close()


# ==========================================================
# Box Plot
# ==========================================================

def boxplot(
    values,
    title,
    ylabel,
    save=None,
):
    """
    Boxplot of parameter estimates.
    """

    plt.figure(figsize=(5, 6))

    plt.boxplot(
        values,
        vert=True,
    )

    plt.title(title)
    plt.ylabel(ylabel)

    plt.tight_layout()

    if save is not None:

        Path(save).parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        plt.savefig(
            save,
            dpi=300,
            bbox_inches="tight",
        )

    plt.close()