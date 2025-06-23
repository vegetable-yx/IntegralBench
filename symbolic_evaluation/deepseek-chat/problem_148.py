import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the square root of pi
sqrt_pi = mp.sqrt(mp.pi)

# Compute pi^(3/2) = pi * sqrt(pi)
pi_power_3_2 = mp.pi * sqrt_pi

# Calculate the denominator: 2 * sqrt(2)
denominator = 2 * mp.sqrt(2)

# Compute the final result: pi^(3/2) / (2 * sqrt(2))
result = pi_power_3_2 / denominator

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))