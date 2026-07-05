"""
Result objects for Lambert W Copula estimation.
"""

from dataclasses import dataclass


@dataclass
class MLEResult:
    """
    Stores the result of maximum likelihood estimation.
    """

    # ======================================================
    # Parameter Estimates
    # ======================================================

    theta: float
    loglik: float

    # ======================================================
    # Estimation Information
    # ======================================================

    method: str = ""

    success: bool = True

    iterations: int | None = None

    # ======================================================
    # Model Selection Criteria
    # ======================================================

    aic: float | None = None

    bic: float | None = None

    # ======================================================
    # Inferential Statistics
    # ======================================================

    std_error: float | None = None

    variance: float | None = None

    # ======================================================
    # Statistical Inference
    # ======================================================

    z_value: float | None = None

    p_value: float | None = None

    ci_lower: float | None = None

    ci_upper: float | None = None

    # ======================================================
    # Pretty Printing
    # ======================================================

    def __str__(self):

        lines = [

            "=" * 60,

            "Maximum Likelihood Estimation",

            "=" * 60,

            f"Method            : {self.method}",

            f"Theta             : {self.theta:.6f}",

            f"Log-Likelihood    : {self.loglik:.6f}",

            f"AIC               : {self.aic:.6f}",

            f"BIC               : {self.bic:.6f}",

            f"Std. Error        : {self.std_error:.6f}"
            if self.std_error is not None
            else "Std. Error        : N/A",

            f"Variance          : {self.variance:.6f}"
            if self.variance is not None
            else "Variance          : N/A",

            f"Z Statistic       : {self.z_value:.6f}"
            if self.z_value is not None
            else "Z Statistic       : N/A",

            f"P-value           : {self.p_value:.6e}"
            if self.p_value is not None
            else "P-value           : N/A",

            f"95% CI Lower      : {self.ci_lower:.6f}"
            if self.ci_lower is not None
            else "95% CI Lower      : N/A",

            f"95% CI Upper      : {self.ci_upper:.6f}"
            if self.ci_upper is not None
            else "95% CI Upper      : N/A",

            f"Success           : {self.success}",

            f"Iterations        : {self.iterations}"
            if self.iterations is not None
            else "Iterations        : N/A",

        ]

        return "\n".join(lines)

    __repr__ = __str__