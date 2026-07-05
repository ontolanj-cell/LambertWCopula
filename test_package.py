"""
Lambert W Copula Package Test
"""

from lambertwcopula import *
import numpy as np


print("=" * 70)
print("Lambert W Copula Package Test")
print("=" * 70)

# ==========================================================
# Constants
# ==========================================================

print("\nConstants")
print("-" * 70)

print(f"Omega          : {OMEGA:.15f}")
print(f"Beta           : {BETA:.15f}")
print(f"Theta Minimum  : {THETA_MIN:.6f}")
print(f"Theta Maximum  : {THETA_MAX:.6f}")


# ==========================================================
# Generating Function
# ==========================================================

print("\nGenerating Function")
print("-" * 70)

u = 0.5

print(f"Psi(0.5)       : {psi(u):.15f}")
print(f"Psi'(0.5)      : {psi_prime(u):.15f}")


# ==========================================================
# Copula
# ==========================================================

print("\nCopula")
print("-" * 70)

theta = 1.0

print(f"CDF            : {cdf(0.5,0.5,theta):.15f}")
print(f"PDF            : {pdf(0.5,0.5,theta):.15f}")


# ==========================================================
# Moments
# ==========================================================

print("\nMoments")
print("-" * 70)

print(f"I0             : {I(0):.15f}")
print(f"I1             : {I(1):.15f}")

print()

print(f"E(UV)          : {mixed_moment(1,1,theta):.15f}")
print(f"Covariance     : {covariance(theta):.15f}")
print(f"Correlation    : {correlation(theta):.15f}")


# ==========================================================
# Dependence Measures
# ==========================================================

print("\nDependence Measures")
print("-" * 70)

print(f"Kendall Tau    : {kendall_tau(theta):.15f}")
print(f"Spearman Rho   : {spearman_rho(theta):.15f}")
print(f"rho = 3 tau ?  : {relation(theta):.15f}")


# ==========================================================
# Closed-form Verification
# ==========================================================

print("\nClosed-form Verification")
print("-" * 70)

poly = polynomial_part(0)
J = J_numeric(0)
I0 = I(0)

print(f"Polynomial     : {poly:.15f}")
print(f"J0             : {J:.15f}")

print()

print(f"I0             : {I0:.15f}")
print(f"Poly + J       : {(poly+J):.15f}")
print(f"Difference     : {abs(I0-(poly+J)):.15e}")


# ==========================================================
# MLE
# ==========================================================

print("\nMaximum Likelihood Estimation")
print("-" * 70)

np.random.seed(123)

u = np.random.rand(500)
v = np.random.rand(500)

score_result = fit_score(u, v)
opt_result = fit_optimizer(u, v)

print("\nScore Equation")
print("-"*40)

print(f"Theta          : {score_result.theta:.10f}")
print(f"LogLik         : {score_result.loglik:.10f}")
print(f"AIC            : {score_result.aic:.10f}")
print(f"BIC            : {score_result.bic:.10f}")
print(f"Std Error      : {score_result.stderr}")
print(f"Variance       : {score_result.variance}")
print(f"Method         : {score_result.method}")
print(f"Success        : {score_result.success}")

print("\nOptimizer")
print("-"*40)

print(f"Theta          : {opt_result.theta:.10f}")
print(f"LogLik         : {opt_result.loglik:.10f}")
print(f"AIC            : {opt_result.aic:.10f}")
print(f"BIC            : {opt_result.bic:.10f}")
print(f"Std Error      : {opt_result.stderr}")
print(f"Variance       : {opt_result.variance}")
print(f"Method         : {opt_result.method}")
print(f"Success        : {opt_result.success}")

print()

print(f"Difference in Theta : {abs(score_result.theta-opt_result.theta):.15f}")


# ==========================================================
# Score Diagnostics
# ==========================================================

print("\nScore Diagnostics")
print("-" * 70)

print(f"Score(thetâ)   : {score(score_result.theta,u,v):.15e}")
print(f"Hessian        : {hessian(score_result.theta,u,v):.15f}")
print(f"Fisher Info    : {fisher_information(score_result.theta,u,v):.15f}")

print("\nAll tests completed successfully.")