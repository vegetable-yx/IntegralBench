import mpmath as mp

# Set internal decimal places for high precision
mp.dps = 15

# Calculate the denominator: 4 multiplied by pi
denominator = 4 * mp.pi

# Compute the result as 1 divided by the denominator
result = 1 / denominator

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))