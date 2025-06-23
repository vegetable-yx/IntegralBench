import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute numerator: 16 * pi
numerator = 16 * mp.pi

# Compute denominator: 3 * sqrt(2)
denominator = 3 * mp.sqrt(2)

# Calculate the result: (16 * pi) / (3 * sqrt(2))
result = numerator / denominator

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))