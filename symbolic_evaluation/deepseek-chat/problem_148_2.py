import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Calculate pi^(3/2)
pi_power = mp.pi ** (3/2)

# Calculate gamma(3/4)
gamma_val = mp.gamma(3/4)

# Square the gamma value
gamma_squared = gamma_val ** 2

# Compute denominator: 2 * sqrt(2) * gamma(3/4)^2
denominator = 2 * mp.sqrt(2) * gamma_squared

# Final result: pi^(3/2) / denominator
result = pi_power / denominator

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))