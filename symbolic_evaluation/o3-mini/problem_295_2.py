import mpmath as mp

# Set internal decimal places to 15 for sufficient precision
mp.dps = 15

# Compute Gamma(1/4)
gamma_val = mp.gamma(mp.mpf(1)/4)

# Raise Gamma(1/4) to the 4th power
gamma_power4 = gamma_val**4

# Compute the denominator: 32 * pi
denominator = 32 * mp.pi

# Calculate the final result: Gamma(1/4)^4 / (32 * pi)
result = gamma_power4 / denominator

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))