import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate the square root of pi
sqrt_pi = mp.sqrt(mp.pi)

# Calculate Gamma(5/4) and Gamma(7/4)
gamma_5_4 = mp.gamma(5/4)
gamma_7_4 = mp.gamma(7/4)

# Compute the numerator: 4 * sqrt(pi) * Gamma(5/4)
numerator = 4 * sqrt_pi * gamma_5_4

# Compute the final result by dividing numerator by Gamma(7/4)
result = numerator / gamma_7_4

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))