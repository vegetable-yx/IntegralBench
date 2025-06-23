import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the square root of pi
sqrt_pi = mp.sqrt(mp.pi)

# Calculate Gamma(1/4)
gamma_1_4 = mp.gamma(mp.mpf(1)/4)

# Calculate Gamma(3/4)
gamma_3_4 = mp.gamma(mp.mpf(3)/4)

# Compute the ratio of gamma functions
gamma_ratio = gamma_1_4 / gamma_3_4

# Multiply by sqrt(pi) to get final result
result = sqrt_pi * gamma_ratio

# Print result to exactly 10 decimal places
print(mp.nstr(result, n=10))