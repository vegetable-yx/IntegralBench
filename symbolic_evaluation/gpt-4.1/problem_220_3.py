import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute the numerator: 5 * pi
numerator = 5 * mp.pi

# Compute the denominator: 4 * sqrt(2)
denominator = 4 * mp.sqrt(2)

# Calculate the result: (5 * pi) / (4 * sqrt(2))
result = numerator / denominator

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))