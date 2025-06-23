import mpmath as mp

# Set internal decimal places to 15 for sufficient precision
mp.dps = 15

# Calculate Gamma(1/4)
gamma_val = mp.gamma(mp.mpf(1)/4)

# Raise to the 4th power
gamma_power = gamma_val**4

# Calculate the denominator: 32 * pi
denominator = 32 * mp.pi

# Compute the final result
result = gamma_power / denominator

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))