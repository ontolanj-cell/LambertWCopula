"""
Data preprocessing utilities
for Lambert W Copula.
"""

import numpy as np
import pandas as pd
from scipy.stats import rankdata


# ==========================================================
# Missing Values
# ==========================================================

def check_missing(data):
    """
    Return the number of missing values
    in each column.
    """

    return data.isnull().sum()


# ==========================================================
# Remove Missing Values
# ==========================================================

def remove_missing(data):
    """
    Remove rows containing missing values.
    """

    return data.dropna().reset_index(drop=True)


# ==========================================================
# Remove Duplicate Rows
# ==========================================================

def remove_duplicates(data):
    """
    Remove duplicated observations.
    """

    return data.drop_duplicates().reset_index(drop=True)


# ==========================================================
# Pseudo-observations
# ==========================================================

def pseudo_observations(data):
    """
    Convert each column into pseudo-observations

        U = rank/(n+1)

    Parameters
    ----------
    data : pandas.DataFrame

    Returns
    -------
    pandas.DataFrame
    """

    n = len(data)

    pseudo = pd.DataFrame(index=data.index)

    for column in data.columns:

        ranks = rankdata(
            data[column],
            method="average"
        )

        pseudo[column] = ranks / (n + 1)

    return pseudo


# ==========================================================
# Validation
# ==========================================================

def validate_pseudo(pseudo):
    """
    Check whether pseudo-observations
    lie strictly inside (0,1).
    """

    return (
        np.all(pseudo.values > 0)
        and
        np.all(pseudo.values < 1)
    )


# ==========================================================
# Summary
# ==========================================================

def preprocessing_summary(data):

    print()

    print("=" * 60)
    print("Preprocessing Summary")
    print("=" * 60)

    print()

    print("Rows :", len(data))

    print()

    print("Missing Values")

    print(check_missing(data))