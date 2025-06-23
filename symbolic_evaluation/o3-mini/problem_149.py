import mpmath as mp

# Set internal precision to 15 decimal places for intermediate calculations
mp.dps = 15

# Calculate gamma(1/4)
gamma_val = mp.gamma(mp.mpf(1)/4)

# Raise gamma(1/4) to the 8th power
gamma_power = gamma_val**8

# Calculate pi squared
pi_squared = mp.pi**2

# Compute denominator: 392 * pi^2
denominator = 392 * pi_squared

# Divide numerator by denominator
result = gamma_power / denominator

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))