import mpmath as mp

# Set internal decimal places for high precision calculation
mp.dps = 15

# Compute gamma(1/4)
gamma_quarter = mp.gamma(0.25)

# Raise gamma(1/4) to the 4th power
gamma_quarter_power4 = gamma_quarter**4

# Compute the denominator: 8 * sqrt(2 * pi)
denom_factor = 8 * mp.sqrt(2 * mp.pi)

# Divide numerator by denominator
result = gamma_quarter_power4 / denom_factor

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))