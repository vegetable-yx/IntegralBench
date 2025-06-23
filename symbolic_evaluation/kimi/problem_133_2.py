import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Compute Gamma(1/4)
gamma_14 = mp.gamma(0.25)

# Square the Gamma function value
gamma_squared = gamma_14 ** 2

# Multiply by 1/2
half_gamma_sq = 0.5 * gamma_squared

# Compute modified Bessel function I_0 at 2.0
bessel_term = mp.besseli(0, 2.0)

# Combine all components for final result
result = half_gamma_sq * bessel_term

# Print result with 10 decimal places
print(mp.nstr(result, n=10))