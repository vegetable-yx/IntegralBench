import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Calculate π raised to the power of 3/2
pi_power = mp.pi ** (3/2)

# Calculate gamma function at 3/4
gamma_val = mp.gamma(3/4)

# Square the gamma value
gamma_squared = gamma_val ** 2

# Compute the final result by division
result = pi_power / gamma_squared

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))