import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate π using mpmath's constant
pi_value = mp.pi

# Compute the sum of π and 2
numerator = pi_value + 2

# Calculate the denominator
denominator = 8

# Combine components to get the final result
result = -numerator / denominator

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))