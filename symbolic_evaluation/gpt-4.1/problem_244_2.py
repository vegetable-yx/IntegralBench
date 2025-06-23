import mpmath as mp

# Set internal precision to 15 decimal places for accurate computation
mp.dps = 15

# Compute Gamma function at 1/4
gamma_val = mp.gamma(1/mp.mpf(4))

# Raise Gamma(1/4) to the 8th power
gamma_power = gamma_val**8

# Compute pi squared
pi_squared = mp.pi**2

# Calculate the denominator: 3840 * pi^2
denominator = 3840 * pi_squared

# Divide the numerator by the denominator
result = gamma_power / denominator

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))