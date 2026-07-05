"""
Residual Visualization
======================

Residual diagnostics for Lambert W Copula.
"""

import matplotlib.pyplot as plt
import numpy as np

from mpl_toolkits.mplot3d import Axes3D


# ==========================================================
# Residual Heat Map
# ==========================================================

def residual_heatmap(
    x,
    y,
    residuals,
    save=None,
):
    """
    Plot residual heat map.
    """

    plt.figure(figsize=(7, 6))

    plt.pcolormesh(
        x,
        y,
        residuals,
        shading="auto",
        cmap="coolwarm",
    )

    plt.colorbar(label="Residual")

    plt.xlabel("u")
    plt.ylabel("v")

    plt.title("Residual Heat Map")

    if save is not None:

        plt.savefig(
            save,
            dpi=300,
            bbox_inches="tight",
        )

    plt.close()


# ==========================================================
# Residual Surface
# ==========================================================

def residual_surface_plot(
    x,
    y,
    residuals,
    save=None,
):
    """
    Plot residual surface.
    """

    fig = plt.figure(figsize=(8, 6))

    ax = fig.add_subplot(
        111,
        projection="3d",
    )

    ax.plot_surface(
        x,
        y,
        residuals,
        cmap="coolwarm",
        linewidth=0,
        antialiased=True,
    )

    ax.set_xlabel("u")
    ax.set_ylabel("v")
    ax.set_zlabel("Residual")

    ax.set_title("Residual Surface")

    if save is not None:

        plt.savefig(
            save,
            dpi=300,
            bbox_inches="tight",
        )

    plt.close()