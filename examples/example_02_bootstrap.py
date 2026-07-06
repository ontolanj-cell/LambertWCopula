"""
Bootstrap Example
"""

from lambertwcopula import *

data = load_csv("../data/data.csv")

u, v = pseudo_observations(data)

result = fit_optimizer(u, v)

estimates = bootstrap_theta(
    u,
    v,
    B=500,
)

summary = bootstrap_summary(
    estimates,
    result.theta,
)

print(summary)