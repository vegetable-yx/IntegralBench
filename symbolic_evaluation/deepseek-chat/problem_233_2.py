import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate gamma function values
gamma_7_4 = mp.gamma(mp.mpf(7)/4)  # Gamma(7/4)
gamma_5_4 = mp.gamma(mp.mpf(5)/4)  # Gamma(5/4)

# Compute the ratio of gamma functions
gamma_ratio = gamma_7_4 / gamma_5_4

# Compute the constant factor: 2 * sqrt(2) * pi
constant_factor = 2 * mp.sqrt(2) * mp.pi

# Multiply to get the final result
result = constant_factor * gamma_ratio

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))