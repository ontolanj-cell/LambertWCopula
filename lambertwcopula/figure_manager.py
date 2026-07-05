"""
Figure Manager
==============

Centralized generation of all figures for the
Lambert W Copula package.

Author: Jay Ontolan
"""

from .visualization import (
    raw_scatter_plot,
    scatter_plot,
    heat_map,
    contour_plot,
    surface_plot,
)

from .visualization_residuals import (
    residual_heatmap,
    residual_surface_plot,
)

from .diagnostic_plots import (
    histogram,
    boxplot,
)

from .likelihood_profile import (
    likelihood_profile,
    likelihood_plot,
)


# ==========================================================
# Likelihood Profile
# ==========================================================

def generate_likelihood_profile(
    u,
    v,
    theta_hat,
):

    theta_grid, loglik_grid = likelihood_profile(
        u,
        v,
    )

    likelihood_plot(
        theta_grid,
        loglik_grid,
        theta_hat=theta_hat,
        save="figures/likelihood_profile.png",
    )

    print("✓ Likelihood profile saved")


# ==========================================================
# Main Figures
# ==========================================================

def generate_main_figures(

    data,

    u,

    v,

    x,

    y,

    Z,

    x_fit,

    y_fit,

    Z_fit,

    R,

):

    raw_scatter_plot(
        data.iloc[:, 0],
        data.iloc[:, 1],
        save="figures/raw_scatter.png",
    )

    scatter_plot(
        u,
        v,
        save="figures/pseudo_scatter.png",
    )

    heat_map(
        x,
        y,
        Z,
        save="figures/empirical_heatmap.png",
    )

    contour_plot(
        x,
        y,
        Z,
        u,
        v,
        save="figures/empirical_contour.png",
    )

    surface_plot(
        x,
        y,
        Z,
        title="Empirical Copula Surface",
        save="figures/empirical_surface.png",
    )

    surface_plot(
        x_fit,
        y_fit,
        Z_fit,
        title="Theoretical Lambert W Copula Surface",
        save="figures/theoretical_surface.png",
    )

    residual_heatmap(
        x,
        y,
        R,
        save="figures/residual_heatmap.png",
    )

    residual_surface_plot(
        x,
        y,
        R,
        save="figures/residual_surface.png",
    )

    print("✓ Main figures saved")


# ==========================================================
# Bootstrap Figures
# ==========================================================

def generate_bootstrap_figures(
    estimates,
):

    histogram(
        estimates,
        title="Bootstrap Distribution of Theta",
        xlabel="Theta",
        save="figures/bootstrap_histogram.png",
    )

    boxplot(
        estimates,
        title="Bootstrap Theta Estimates",
        ylabel="Theta",
        save="figures/bootstrap_boxplot.png",
    )

    print("✓ Bootstrap figures saved")


# ==========================================================
# Cross Validation Figures
# ==========================================================

def generate_cv_figures(
    cv,
):

    histogram(
        cv["theta_values"],
        title="Cross Validation Theta Distribution",
        xlabel="Theta",
        save="figures/cv_histogram.png",
    )

    boxplot(
        cv["theta_values"],
        title="Cross Validation Theta Estimates",
        ylabel="Theta",
        save="figures/cv_boxplot.png",
    )

    print("✓ Cross-validation figures saved")


# ==========================================================
# Generate Everything
# ==========================================================

def generate_all_figures(context):
    """
    Generate every figure used in the analysis.
    """

    data = context.data

    u = context.u
    v = context.v

    x = context.empirical["x"]
    y = context.empirical["y"]
    Z = context.empirical["surface"]

    x_fit = context.theoretical["x"]
    y_fit = context.theoretical["y"]
    Z_fit = context.theoretical["surface"]

    R = context.analysis["residuals"]["surface"]

    estimates = context.estimates

    cv = context.cv

    theta_hat = context.result.theta

    print("\nGenerating Figures")
    print("-" * 70)

    generate_likelihood_profile(
        u,
        v,
        theta_hat,
    )

    generate_main_figures(
        data,
        u,
        v,
        x,
        y,
        Z,
        x_fit,
        y_fit,
        Z_fit,
        R,
    )

    generate_bootstrap_figures(
        estimates,
    )

    generate_cv_figures(
        cv,
    )