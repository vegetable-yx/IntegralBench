import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define the function to be differentiated
def f(alpha, beta, gamma):
    # Compute the ratio of gamma functions
    gamma_ratio = mp.gamma(alpha) * mp.gamma(beta) / mp.gamma(alpha + beta)
    # Compute the hypergeometric function _2F_1(gamma, alpha, alpha+beta, -1)
    hyp_val = mp.hyp2f1(gamma, alpha, alpha + beta, -1)
    return gamma_ratio * hyp_val

# Point of evaluation
alpha0 = mp.mpf(1)/2
beta0 = mp.mpf(2)
gamma0 = mp.mpf(2)

# Step size for finite differences
h = mp.mpf('1e-5')

# Compute the base value at the evaluation point
f0 = f(alpha0, beta0, gamma0)

# Compute second partial derivative with respect to beta (d^2/db^2)
f_bp = f(alpha0, beta0 + h, gamma0)  # beta + h
f_bm = f(alpha0, beta0 - h, gamma0)  # beta - h
d2f_db2 = (f_bp - 2*f0 + f_bm) / (h**2)

# Compute mixed partial derivative with respect to alpha and beta (d^2/(da db))
f_apbp = f(alpha0 + h, beta0 + h, gamma0)  # alpha+h, beta+h
f_apbm = f(alpha0 + h, beta0 - h, gamma0)  # alpha+h, beta-h
f_ambp = f(alpha0 - h, beta0 + h, gamma0)  # alpha-h, beta+h
f_ambm = f(alpha0 - h, beta0 - h, gamma0)  # alpha-h, beta-h
d2f_dadb = (f_apbp - f_apbm - f_ambp + f_ambm) / (4 * h**2)

# Compute mixed partial derivative with respect to alpha and gamma (d^2/(da dg))
f_apgp = f(alpha0 + h, beta0, gamma0 + h)  # alpha+h, gamma+h
f_apgm = f(alpha0 + h, beta0, gamma0 - h)  # alpha+h, gamma-h
f_amgp = f(alpha0 - h, beta0, gamma0 + h)  # alpha-h, gamma+h
f_amgm = f(alpha0 - h, beta0, gamma0 - h)  # alpha-h, gamma-h
d2f_dadg = (f_apgp - f_apgm - f_amgp + f_amgm) / (4 * h**2)

# Compute mixed partial derivative with respect to beta and gamma (d^2/(db dg))
f_bpgp = f(alpha0, beta0 + h, gamma0 + h)  # beta+h, gamma+h
f_bpgm = f(alpha0, beta0 + h, gamma0 - h)  # beta+h, gamma-h
f_bmgp = f(alpha0, beta0 - h, gamma0 + h)  # beta-h, gamma+h
f_bmgm = f(alpha0, beta0 - h, gamma0 - h)  # beta-h, gamma-h
d2f_dbdg = (f_bpgp - f_bpgm - f_bmgp + f_bmgm) / (4 * h**2)

# Combine derivatives according to the operator:
# [d2/(da db) - 2*d2/(db^2) - d2/(da dg) + 2*d2/(db dg)]
result = d2f_dadb - 2*d2f_db2 - d2f_dadg + 2*d2f_dbdg

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))