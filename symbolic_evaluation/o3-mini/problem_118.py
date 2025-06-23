import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute Gamma(1/4)
gamma_quarter = mp.gamma(1/4)

# Raise to the 8th power
gamma_quarter_power8 = gamma_quarter**8

# Compute pi squared
pi_squared = mp.pi**2

# Compute denominator: 128 * pi^2
denominator = 128 * pi_squared

# Compute the final result: Gamma(1/4)^8 / (128 * pi^2)
result = gamma_quarter_power8 / denominator

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))