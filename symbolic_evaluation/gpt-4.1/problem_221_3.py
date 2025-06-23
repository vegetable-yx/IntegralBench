import mpmath as mp

# Set internal decimal places for calculation to 15
mp.dps = 15

# Calculate the numerator: 3 * pi
numerator = 3 * mp.pi

# Calculate the denominator: 16
denominator = 16

# Compute the result: (3 * pi) / 16
result = numerator / denominator

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))