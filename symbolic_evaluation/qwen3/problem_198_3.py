import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate Gamma(3/4)
gamma_34 = mp.gamma(mp.mpf(3)/4)

# Square the Gamma function result
gamma_squared = gamma_34 ** 2

# Calculate square root of 2
sqrt_2 = mp.sqrt(2)

# Combine components for final result
result = sqrt_2 * gamma_squared

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))