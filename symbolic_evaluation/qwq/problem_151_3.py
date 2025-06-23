import mpmath as mp

mp.dps = 15  # Set internal precision

# Calculate π squared
pi_squared = mp.pi ** 2

# Calculate Gamma(3/4) and square it
gamma_3_4 = mp.gamma(mp.mpf(3)/4)
gamma_squared = gamma_3_4 ** 2

# Calculate square root of 2
sqrt2 = mp.sqrt(2)

# Combine components for denominator
denominator = sqrt2 * gamma_squared

# Compute final result
result = pi_squared / denominator

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))