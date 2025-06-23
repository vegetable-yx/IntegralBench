import mpmath as mp

# Set internal precision to 15 decimal places for calculations
mp.dps = 15

# Calculate the numerator: 4 * pi
numerator = 4 * mp.pi

# Calculate the denominator: 3 * sqrt(3)
denominator = 3 * mp.sqrt(3)

# Compute the result: (4 * pi) / (3 * sqrt(3))
result = numerator / denominator

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))