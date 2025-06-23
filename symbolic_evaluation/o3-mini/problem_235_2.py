import mpmath as mp

# Set internal decimal places to 15 for precision
mp.dps = 15

# Calculate Gamma(1/4)
gamma_14 = mp.gamma(mp.mpf(1)/4)

# Square the Gamma(1/4) value
gamma_sq = gamma_14 ** 2

# Compute sqrt(2)
sqrt2 = mp.sqrt(2)

# Multiply to get numerator: sqrt(2) * [Gamma(1/4)]^2
numerator = sqrt2 * gamma_sq

# Compute sqrt(pi)
sqrt_pi = mp.sqrt(mp.pi)

# Calculate denominator: 2 * sqrt(pi)
denominator = 2 * sqrt_pi

# Final result: numerator / denominator
result = numerator / denominator

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))