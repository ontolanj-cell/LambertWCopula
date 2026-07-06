"""
Cross Validation Example
"""

from lambertwcopula import *

data = load_csv("../data/data.csv")

u, v = pseudo_observations(data)

cv = kfold_cv(
    u,
    v,
)

print(cv)