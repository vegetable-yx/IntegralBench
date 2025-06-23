import mpmath as mp

# Set internal decimal precision to 15 for accurate calculations
mp.dps = 15

# Compute Gamma(3/4)
gamma_val = mp.gamma(3/4)

# Raise Gamma(3/4) to the 4th power
gamma_power = gamma_val**4

# Calculate the numerator: 11 * [Gamma(3/4)]^4
numerator = 11 * gamma_power

# Calculate the denominator: 16 * sqrt(pi)
denominator = 16 * mp.sqrt(mp.pi)

# Compute the final result: numerator / denominator
result = numerator / denominator

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))