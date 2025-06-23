import mpmath as mp

mp.dps = 15  # Set internal precision

# Compute Gamma(1/4)
gamma_val = mp.gamma(mp.mpf(1)/4)

# Calculate numerator: Gamma(1/4)^4
numerator = gamma_val**4

# Calculate denominator components
sqrt2 = mp.sqrt(2)
denominator = 4 * sqrt2 * mp.pi

# Compute final result
result = numerator / denominator

# Print with 10 decimal precision
print(mp.nstr(result, n=10))