import mpmath as mp

# Set internal decimal precision to 15 to ensure accurate computation
mp.dps = 15

# Calculate numerator: 7 * pi
numerator = 7 * mp.pi

# Calculate denominator: 3 * sqrt(3)
denominator = 3 * mp.sqrt(3)

# Compute the result: (7 * pi) / (3 * sqrt(3))
result = numerator / denominator

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))