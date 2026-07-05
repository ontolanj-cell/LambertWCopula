"""
Automatic copula comparison.
"""

from .gaussian import fit_gaussian


def fit_all_copulas(u, v, lambert):

    models = [

        lambert,

        fit_gaussian(
            u,
            v,
        ),

    ]

    return models


def best_model(models):

    return min(
        models,
        key=lambda m: m["AIC"],
    )


def print_comparison(models):

    print("=" * 93)

    print(
        f"{'Model':<15}"
        f"{'Theta':>12}"
        f"{'LogLik':>12}"
        f"{'AIC':>12}"
        f"{'BIC':>12}"
    )

    print("=" * 93)

    for m in models:

        print(
            f"{m['Model']:<15}"
            f"{m['Theta']:>12.4f}"
            f"{m['LogLik']:>12.4f}"
            f"{m['AIC']:>12.4f}"
            f"{m['BIC']:>12.4f}"
        )

    print("=" * 93)