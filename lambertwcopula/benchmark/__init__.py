"""
Benchmark copulas for model comparison.
"""

from .gaussian import fit_gaussian

from .compare import (
    fit_all_copulas,
    best_model,
    print_comparison,
)

__all__ = [
    "fit_gaussian",
    "fit_all_copulas",
    "best_model",
    "print_comparison",
]