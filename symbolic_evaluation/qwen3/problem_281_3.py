import mpmath as mp
mp.dps = 15  # Set decimal places for internal precision

# Compute Gamma(1/4)
gamma_1_4 = mp.gamma(mp.mpf(1)/4)

# Square the Gamma function value
gamma_sq = gamma_1_4 ** 2

# Calculate denominator components: 2*sqrt(2π)
sqrt_2pi = mp.sqrt(2 * mp.pi)
denominator = 2 * sqrt_2pi

# Compute hyperbolic cosine of 4
cosh_4 = mp.cosh(4)

# Combine components for final result
numerator = gamma_sq * cosh_4
result = numerator / denominator

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))