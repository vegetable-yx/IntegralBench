import mpmath as mp

# Set internal decimal places to 15 for sufficient precision
mp.dps = 15

# Compute numerator: 5 * pi
numerator = 5 * mp.pi

# Compute denominator: 4 * sqrt(2)
denominator = 4 * mp.sqrt(2)

# Calculate the final result: (5 * pi) / (4 * sqrt(2))
result = numerator / denominator

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))