import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the numerator: pi
numerator = mp.pi

# Calculate the denominator: 2 * sqrt(2)
sqrt2 = mp.sqrt(2)
denominator = 2 * sqrt2

# Compute the result: pi / (2 * sqrt(2))
result = numerator / denominator

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))