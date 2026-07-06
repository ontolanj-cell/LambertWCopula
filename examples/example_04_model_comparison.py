"""
Model Comparison Example
"""

from lambertwcopula import *

data = load_csv("../data/data.csv")

u, v = pseudo_observations(data)

result = fit_optimizer(
    u,
    v,
)

lambert = model_summary(
    result,
)

models = fit_all_copulas(
    u,
    v,
    lambert,
)

print_comparison(models)