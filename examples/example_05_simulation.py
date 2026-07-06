"""
Simulation Example
"""

from lambertwcopula import *

samples = simulate(
    theta=2.5,
    n=1000,
)

print(samples[:10])