"""
Visualization Utilities
=======================

Visualization functions for the Lambert W Copula package.
"""

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D


# ==========================================================
# Raw Data Scatter Plot
# ==========================================================

def raw_scatter_plot(x, y, save=None):
    """
    Scatter plot of the original data.
    """

    plt.figure(figsize=(7, 7))

    plt.scatter(
        x,
        y,
        s=20,
        alpha=0.75,
        edgecolor="black",
        linewidth=0.25,
    )

    plt.xlabel("Temperature", fontsize=13)
    plt.ylabel("Precipitation", fontsize=13)

    plt.title(
        "Raw Data Scatter Plot",
        fontsize=16,
        fontweight="bold",
    )

    plt.grid(alpha=0.30)

    plt.tight_layout()

    if save is not None:
        plt.savefig(
            save,
            dpi=300,
            bbox_inches="tight",
        )

    plt.show()


# ==========================================================
# Scatter Plot
# ==========================================================

def scatter_plot(u, v, save=None):
    """
    Scatter plot of pseudo-observations.
    """

    plt.figure(figsize=(7, 7))

    plt.scatter(
        u,
        v,
        s=18,
        alpha=0.75,
        edgecolor="black",
        linewidth=0.25,
    )

    plt.xlabel("U", fontsize=13)
    plt.ylabel("V", fontsize=13)

    plt.title(
        "Pseudo-observations",
        fontsize=16,
        fontweight="bold",
    )

    plt.xlim(0, 1)
    plt.ylim(0, 1)

    plt.grid(alpha=0.30)

    plt.tight_layout()

    if save is not None:
        plt.savefig(
            save,
            dpi=300,
            bbox_inches="tight",
        )

    plt.show()


# ==========================================================
# Heat Map
# ==========================================================

def heat_map(x, y, Z, save=None):
    """
    Heat map of the empirical copula.
    """

    plt.figure(figsize=(8, 6))

    image = plt.imshow(
        Z,
        origin="lower",
        extent=[0, 1, 0, 1],
        aspect="auto",
        cmap="viridis",
    )

    plt.colorbar(image)

    plt.xlabel("U", fontsize=13)
    plt.ylabel("V", fontsize=13)

    plt.title(
        "Empirical Copula Heat Map",
        fontsize=16,
        fontweight="bold",
    )

    plt.tight_layout()

    if save is not None:
        plt.savefig(
            save,
            dpi=300,
            bbox_inches="tight",
        )

    plt.show()


# ==========================================================
# Contour Plot
# ==========================================================

def contour_plot(x, y, Z, u=None, v=None, save=None):
    """
    Empirical copula contour plot with pseudo-observations.
    """

    X, Y = np.meshgrid(x, y)

    plt.figure(figsize=(8, 7))

    contour = plt.contourf(
        X,
        Y,
        Z,
        levels=20,
        cmap="viridis",
    )

    plt.contour(
        X,
        Y,
        Z,
        levels=20,
        colors="black",
        linewidths=0.30,
        alpha=0.40,
    )

    plt.colorbar(contour)

    if u is not None and v is not None:

        plt.scatter(
            u,
            v,
            s=18,
            color="lightgray",
            edgecolor="white",
            linewidth=0.25,
            alpha=0.80,
            label="Pseudo-observations",
        )

        plt.legend(
            loc="lower left",
            fontsize=11,
        )

    plt.xlabel("U", fontsize=13)
    plt.ylabel("V", fontsize=13)

    plt.title(
        "Empirical Copula Contour",
        fontsize=16,
        fontweight="bold",
    )

    plt.xlim(0, 1)
    plt.ylim(0, 1)

    plt.tight_layout()

    if save is not None:
        plt.savefig(
            save,
            dpi=300,
            bbox_inches="tight",
        )

    plt.show()


# ==========================================================
# 3D Surface Plot
# ==========================================================

def surface_plot(
    x,
    y,
    Z,
    title="Empirical Copula Surface",
    save=None,
):
    """
    3D surface plot of a copula surface.
    """

    X, Y = np.meshgrid(x, y)

    fig = plt.figure(figsize=(10, 8))

    ax = fig.add_subplot(111, projection="3d")

    surface = ax.plot_surface(
        X,
        Y,
        Z,
        cmap="viridis",
        edgecolor="none",
        antialiased=True,
    )

    fig.colorbar(
        surface,
        shrink=0.60,
        aspect=15,
        pad=0.10,
    )

    ax.set_xlabel("U", fontsize=12)
    ax.set_ylabel("V", fontsize=12)
    ax.set_zlabel("C(u,v)", fontsize=12)

    ax.set_title(
        title,
        fontsize=16,
        fontweight="bold",
    )

    ax.view_init(
        elev=30,
        azim=-135,
    )

    plt.tight_layout()

    if save is not None:
        plt.savefig(
            save,
            dpi=300,
            bbox_inches="tight",
        )

    plt.show()