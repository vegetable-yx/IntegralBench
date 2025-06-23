import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Compute the square root of pi
sqrt_pi = mp.sqrt(mp.pi)

# Calculate Gamma(1/4) and square it
gamma_1_4 = mp.gamma(mp.mpf(1)/4)
gamma_1_4_squared = gamma_1_4 ** 2

# Compute the numerator: sqrt(pi) * [Gamma(1/4)]^2
numerator = sqrt_pi * gamma_1_4_squared

# Calculate Gamma(3/4)
gamma_3_4 = mp.gamma(mp.mpf(3)/4)

# Compute the denominator: sqrt(2) * Gamma(3/4)
denominator = mp.sqrt(2) * gamma_3_4

# Calculate the final result
result = numerator / denominator

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))