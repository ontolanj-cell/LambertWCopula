import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def empirical_copula(pseudo):

    print("\nComputing Empirical Copula...")

    U = pseudo["U"].values
    V = pseudo["V"].values

    n = len(U)

    # ----------------------------------------
    # High-resolution grid
    # ----------------------------------------

    grid = np.linspace(0, 1, 101)

    X, Y = np.meshgrid(grid, grid)

    C = np.zeros_like(X)

    # ----------------------------------------
    # Empirical Copula
    # ----------------------------------------

    for i in range(len(grid)):
        for j in range(len(grid)):

            C[i, j] = np.mean(
                (U <= grid[j]) &
                (V <= grid[i])
            )

    # ----------------------------------------
    # Save matrix
    # ----------------------------------------

    empirical = pd.DataFrame(
        C,
        index=grid,
        columns=grid
    )

    empirical.to_csv(
        "results/EmpiricalCopulaSurface.csv"
    )

    # ========================================
    # Publication Contour Plot
    # ========================================

    plt.figure(figsize=(8, 6), dpi=300)

    contour = plt.contourf(
        X,
        Y,
        C,
        levels=30,
        cmap="viridis"
    )

    plt.scatter(
        U,
        V,
        s=8,
        c="white",
        edgecolors="black",
        linewidths=0.2,
        alpha=0.45,
        label="Pseudo-observations"
    )

    plt.xlabel("U", fontsize=12)
    plt.ylabel("V", fontsize=12)

    plt.title(
        "Empirical Copula Contour",
        fontsize=14
    )

    plt.colorbar(contour)

    plt.legend()

    plt.tight_layout()

    plt.savefig(
        "figures/EmpiricalContour.png",
        dpi=300
    )

    plt.close()

    # ========================================
    # Publication Surface Plot
    # ========================================

    fig = plt.figure(
        figsize=(9,7),
        dpi=300
    )

    ax = fig.add_subplot(
        111,
        projection="3d"
    )

    surf = ax.plot_surface(

        X,

        Y,

        C,

        cmap="viridis",

        linewidth=0,

        antialiased=True

    )

    fig.colorbar(
        surf,
        shrink=0.6,
        aspect=12
    )

    ax.set_xlabel("U")
    ax.set_ylabel("V")
    ax.set_zlabel("C(u,v)")

    ax.set_title(
        "Empirical Copula Surface"
    )

    plt.tight_layout()

    plt.savefig(
        "figures/EmpiricalSurface.png",
        dpi=300
    )

    plt.close()

    print("Empirical Copula Completed.")