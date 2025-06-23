import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Compute Gamma(1/4)
gamma_val = mp.gamma(mp.mpf(1)/4)

# Raise to the 4th power
gamma_fourth = gamma_val**4

# Compute denominator: 8 * sqrt(2 * pi)
denominator = 8 * mp.sqrt(2 * mp.pi)

# Compute the final result
result = gamma_fourth / denominator

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))