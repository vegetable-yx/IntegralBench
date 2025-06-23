import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate numerator: 8 * pi
numerator = 8 * mp.pi

# Calculate denominator: 3 * sqrt(3)
denominator = 3 * mp.sqrt(3)

# Compute the result: (8 * pi) / (3 * sqrt(3))
result = numerator / denominator

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))