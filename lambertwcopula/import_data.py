"""
Import utilities for Lambert W Copula
"""

from pathlib import Path
import pandas as pd


def load_csv(filename):
    """
    Load a CSV dataset.

    Parameters
    ----------
    filename : str or Path

    Returns
    -------
    pandas.DataFrame
    """

    filename = Path(filename)

    if not filename.exists():
        raise FileNotFoundError(
            f"{filename} does not exist."
        )

    return pd.read_csv(filename)