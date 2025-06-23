import mpmath as mp

# Set the precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate Gamma(1/4)
gamma_1_4 = mp.gamma(1/4)

# Compute the numerator: Gamma(1/4)^4
numerator = gamma_1_4**4

# Compute the denominator: 8 * sqrt(2π)
denominator = 8 * mp.sqrt(2 * mp.pi)

# Calculate the final result
result = numerator / denominator

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))