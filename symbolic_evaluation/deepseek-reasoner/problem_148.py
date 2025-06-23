import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate π squared
pi_squared = mp.pi ** 2

# Calculate the denominator: 2 * sqrt(2)
sqrt_two = mp.sqrt(2)
denominator = 2 * sqrt_two

# Compute the final result
result = pi_squared / denominator

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))