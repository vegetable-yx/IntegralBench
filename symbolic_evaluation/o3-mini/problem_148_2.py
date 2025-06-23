import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute Gamma(1/4)
gamma_val = mp.gamma(mp.mpf('0.25'))

# Raise Gamma(1/4) to the 4th power
gamma_power = gamma_val**4

# Compute the denominator: 16 * sqrt(2) * pi
denom = 16 * mp.sqrt(2) * mp.pi

# Divide numerator by denominator to get the result
result = gamma_power / denom

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))