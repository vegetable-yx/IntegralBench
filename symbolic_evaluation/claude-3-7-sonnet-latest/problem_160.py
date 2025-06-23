import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define the parameter 'a' (using an arbitrary value since not specified)
a = 1.0  # Can be adjusted to any non-negative value

# Compute the square root of a
sqrt_a = mp.sqrt(a)

# Multiply by 2 and by pi to get the result
result = 2 * sqrt_a * mp.pi

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))