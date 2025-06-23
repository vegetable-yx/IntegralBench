import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute gamma(1/4)
gamma_val = mp.gamma(1/4)

# Compute gamma(1/4) raised to the 4th and 8th powers
gamma_4 = gamma_val**4
gamma_8 = gamma_val**8

# Compute pi squared and pi to the fourth power
pi_sq = mp.pi**2
pi_fourth = mp.pi**4

# Compute the three terms in the numerator
term1 = gamma_8
term2 = 16 * pi_sq * gamma_4
term3 = 64 * pi_fourth

# Combine terms to form the numerator
numerator = term1 + term2 - term3

# Compute the denominator
denominator = 512 * pi_sq

# Final result
result = numerator / denominator

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))