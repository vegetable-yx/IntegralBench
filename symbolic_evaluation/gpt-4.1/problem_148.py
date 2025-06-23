import mpmath as mp

# Set internal decimal places for calculation
mp.dps = 15

# Compute Gamma(1/4)
gamma_val = mp.gamma(mp.mpf(1)/4)

# Raise to the fourth power
gamma_power = gamma_val**4

# Compute the constant factor: sqrt(2)/48
constant_factor = mp.sqrt(2) / 48

# Multiply to get the final result
result = constant_factor * gamma_power

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))