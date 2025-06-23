import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate Gamma(5/4)
gamma_5_4 = mp.gamma(5/4)

# Calculate Gamma(7/4)
gamma_7_4 = mp.gamma(7/4)

# Calculate Gamma(3/4)
gamma_3_4 = mp.gamma(3/4)

# Compute term1: 16 * Gamma(5/4) * Gamma(7/4)
term1 = 16 * gamma_5_4 * gamma_7_4

# Compute term2: 24 * Gamma(5/4) * Gamma(3/4)
term2 = 24 * gamma_5_4 * gamma_3_4

# Final result: term1 - term2
result = term1 - term2

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))