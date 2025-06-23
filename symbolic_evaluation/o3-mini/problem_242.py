import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Define numerator: pi
numerator = mp.pi

# Compute denominator: 12 * sqrt(3)
denominator = 12 * mp.sqrt(3)

# Calculate the result: pi / (12 * sqrt(3))
result = numerator / denominator

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))