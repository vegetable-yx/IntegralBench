import mpmath as mp

# Set internal decimal places to 15 for sufficient precision
mp.dps = 15

# Calculate Gamma(1/4)
gamma_quarter = mp.gamma(1/4)

# Raise Gamma(1/4) to the 8th power
gamma_quarter_power8 = gamma_quarter**8

# Compute pi squared
pi_squared = mp.pi**2

# Calculate denominator: 128 * pi^2
denominator = 128 * pi_squared

# Divide numerator by denominator to get final result
result = gamma_quarter_power8 / denominator

# Print result to 10 decimal places
print(mp.nstr(result, n=10))