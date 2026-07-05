"""
Analysis Context
================

Stores the complete state of a Lambert W Copula analysis.

Author: Jay Ontolan
"""

from dataclasses import dataclass, field


@dataclass
class AnalysisContext:
    """
    Container for the complete analysis.
    """

    # ======================================================
    # Data
    # ======================================================

    data: object = None

    pseudo: object = None

    u: object = None

    v: object = None

    # ======================================================
    # Empirical Surface
    # ======================================================

    empirical: dict = field(default_factory=dict)

    # ======================================================
    # Theoretical Surface
    # ======================================================

    theoretical: dict = field(default_factory=dict)

    # ======================================================
    # MLE Result
    # ======================================================

    result: object = None

    # ======================================================
    # Goodness-of-Fit
    # ======================================================

    analysis: dict = field(default_factory=dict)

    # ======================================================
    # Bootstrap
    # ======================================================

    estimates: object = None

    bootstrap: dict = field(default_factory=dict)

    # ======================================================
    # Cross Validation
    # ======================================================

    cv: dict = field(default_factory=dict)

    # ======================================================
    # Benchmark Models
    # ======================================================

    models: list = field(default_factory=list)

    winner: dict = field(default_factory=dict)