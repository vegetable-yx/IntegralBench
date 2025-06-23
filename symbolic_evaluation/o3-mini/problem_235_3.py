import mpmath as mp

# Set internal decimal places for high precision
mp.dps = 15

# Calculate gamma(1/4)
gamma_val = mp.gamma(mp.mpf(1)/4)

# Square the gamma value
gamma_sq = gamma_val ** 2

# Calculate sqrt(2)
sqrt2 = mp.sqrt(2)

# Calculate numerator: sqrt(2) * [gamma(1/4)]^2
numerator = sqrt2 * gamma_sq

# Calculate sqrt(pi)
sqrt_pi = mp.sqrt(mp.pi)

# Calculate denominator: 2 * sqrt(pi)
denominator = 2 * sqrt_pi

# Final result: numerator divided by denominator
result = numerator / denominator

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))