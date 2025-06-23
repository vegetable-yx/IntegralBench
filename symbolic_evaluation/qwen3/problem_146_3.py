import mpmath as mp

mp.dps = 15  # Set internal precision

# Calculate Gamma(1/4)
gamma_1_4 = mp.gamma(mp.mpf('0.25'))

# Compute Gamma(1/4)^4
numerator = gamma_1_4**4

# Calculate denominator components
sqrt_2pi = mp.sqrt(2 * mp.pi)
denominator = 8 * sqrt_2pi

# Final result calculation
result = numerator / denominator

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))