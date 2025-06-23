import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute Gamma(1/4)
gamma_14 = mp.gamma(mp.mpf(1)/4)

# Square the Gamma(1/4) value
gamma_sq = gamma_14 ** 2

# Compute the denominator: 2 * sqrt(pi)
denominator = 2 * mp.sqrt(mp.pi)

# Compute the multiplicative factor: Gamma(1/4)^2 / (2*sqrt(pi))
factor = gamma_sq / denominator

# Compute Bessel functions at x=1
J_neg14 = mp.besselj(-mp.mpf(1)/4, 1)  # J_{-1/4}(1)
J_14 = mp.besselj(mp.mpf(1)/4, 1)      # J_{1/4}(1)

# Sum the Bessel functions
bessel_sum = J_neg14 + J_14

# Multiply by the precomputed factor
result = factor * bessel_sum

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))