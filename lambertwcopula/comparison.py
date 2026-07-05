"""
Model Comparison
Lambert W Copula
"""

from operator import itemgetter


# ==========================================================
# Model Summary
# ==========================================================

def model_summary(
    name,
    theta,
    loglik,
    aic,
    bic,
    rmse,
    mae,
):
    """
    Create a standardized model summary.
    """

    return {

        "Model": name,

        "Theta": theta,

        "LogLik": loglik,

        "AIC": aic,

        "BIC": bic,

        "RMSE": rmse,

        "MAE": mae,

    }


# ==========================================================
# Compare Models
# ==========================================================

def compare_models(*models):
    """
    Return a list of fitted model summaries.
    """

    return list(models)


# ==========================================================
# Rank Models
# ==========================================================

def rank_models(models):
    """
    Rank models by

    1. Lowest AIC
    2. Lowest BIC
    3. Lowest RMSE
    4. Highest LogLik
    """

    return sorted(

        models,

        key=lambda x: (

            x["AIC"],

            x["BIC"],

            x["RMSE"],

            -x["LogLik"],

        ),

    )


# ==========================================================
# Best Model
# ==========================================================

def best_model(models):
    """
    Return the best model.
    """

    return rank_models(models)[0]


# ==========================================================
# Comparison Table
# ==========================================================

def comparison_table(models):
    """
    Return formatted comparison table.
    """

    models = rank_models(models)

    header = (

        f"{'Model':15s}"

        f"{'Theta':>10s}"

        f"{'LogLik':>12s}"

        f"{'AIC':>12s}"

        f"{'BIC':>12s}"

        f"{'RMSE':>12s}"

        f"{'MAE':>12s}"

    )

    lines = [

        "=" * len(header),

        header,

        "=" * len(header),

    ]

    for m in models:

        lines.append(

            f"{m['Model']:15s}"

            f"{m['Theta']:10.4f}"

            f"{m['LogLik']:12.4f}"

            f"{m['AIC']:12.4f}"

            f"{m['BIC']:12.4f}"

            f"{m['RMSE']:12.4f}"

            f"{m['MAE']:12.4f}"

        )

    lines.append("=" * len(header))

    return "\n".join(lines)


# ==========================================================
# Print Comparison
# ==========================================================

def print_comparison(models):
    """
    Pretty print comparison table.
    """

    print(comparison_table(models))