"""
Automatic interpretation engine for copula analysis.

Author: Jay Ontolan
"""


# ==========================================================
# Parameter Interpretation
# ==========================================================

def interpret_parameter(result):

    lines = []

    if result.p_value < 0.01:

        lines.append(
            "The dependence parameter is highly statistically significant (p < 0.01)."
        )

    elif result.p_value < 0.05:

        lines.append(
            "The dependence parameter is statistically significant (p < 0.05)."
        )

    else:

        lines.append(
            "The dependence parameter is not statistically significant at the 5% significance level."
        )

    if result.theta > 0:

        lines.append(
            "The estimated dependence indicates positive association between the variables."
        )

    elif result.theta < 0:

        lines.append(
            "The estimated dependence indicates negative association between the variables."
        )

    else:

        lines.append(
            "The estimated dependence indicates independence."
        )

    return lines


# ==========================================================
# Local Fit
# ==========================================================

def interpret_local_fit(rmse, mae):

    lines = []

    if rmse < 0.03:

        lines.append(
            "RMSE indicates excellent agreement between the empirical and theoretical copula surfaces."
        )

    elif rmse < 0.06:

        lines.append(
            "RMSE indicates good agreement between the empirical and theoretical copula surfaces."
        )

    else:

        lines.append(
            "RMSE suggests noticeable discrepancies between the empirical and theoretical copula surfaces."
        )

    if mae < 0.03:

        lines.append(
            "MAE confirms that average pointwise errors are very small."
        )

    else:

        lines.append(
            "MAE indicates moderate pointwise approximation errors."
        )

    return lines


# ==========================================================
# Global Fit
# ==========================================================

def interpret_global_fit(result):

    lines = []

    lines.append(
        f"The model achieved a log-likelihood of {result.loglik:.4f}."
    )

    if result.aic < 0:

        lines.append(
            "The negative AIC suggests a well-fitting model relative to its complexity."
        )

    else:

        lines.append(
            "AIC should be compared with competing copula models for model selection."
        )

    return lines


# ==========================================================
# Bootstrap
# ==========================================================

def interpret_bootstrap(summary):

    lines = []

    if abs(summary["bias"]) < 0.10:

        lines.append(
            "Bootstrap results indicate negligible estimation bias."
        )

    else:

        lines.append(
            "Bootstrap results indicate noticeable estimation bias."
        )

    return lines


# ==========================================================
# Cross Validation
# ==========================================================

def interpret_cv(cv):

    lines = []

    if cv["theta_cv"] < 20:

        lines.append(
            "Cross-validation indicates highly stable parameter estimates."
        )

    elif cv["theta_cv"] < 40:

        lines.append(
            "Cross-validation indicates reasonably stable parameter estimates."
        )

    else:

        lines.append(
            "Cross-validation suggests considerable variability across folds."
        )

    return lines


# ==========================================================
# Overall Report
# ==========================================================

def interpretation_report(
    result,
    rmse,
    mae,
    bootstrap,
    cv,
):

    report = []

    report.extend(
        interpret_parameter(result)
    )

    report.extend(
        interpret_local_fit(
            rmse,
            mae,
        )
    )

    report.extend(
        interpret_global_fit(result)
    )

    report.extend(
        interpret_bootstrap(bootstrap)
    )

    report.extend(
        interpret_cv(cv)
    )

    return report