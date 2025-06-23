import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Compute the square root of pi
sqrt_pi = mp.sqrt(mp.pi)

# Compute the square root of 2
sqrt_2 = mp.sqrt(2)

# Compute the Gamma function values
gamma_3_4 = mp.gamma(mp.mpf(3)/4)
gamma_5_4 = mp.gamma(mp.mpf(5)/4)

# Calculate the ratio of Gamma functions
gamma_ratio = gamma_3_4 / gamma_5_4

# Combine all components to get the final result
result = (sqrt_pi / sqrt_2) * gamma_ratio

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))