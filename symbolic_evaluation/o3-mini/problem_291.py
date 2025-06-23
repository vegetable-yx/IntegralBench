import mpmath as mp

# Set internal decimal places for precision
mp.dps = 15

# Compute Gamma(1/4)
gamma_val = mp.gamma(1/4)

# Raise Gamma(1/4) to the 8th power
gamma_8th = gamma_val**8

# Compute the denominator: 2048 * π²
denominator = 2048 * mp.pi**2

# Calculate the final result
result = gamma_8th / denominator

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))