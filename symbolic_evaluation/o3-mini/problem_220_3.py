import mpmath as mp

# Set internal decimal places for high precision calculation
mp.dps = 15

# Calculate numerator: 5 * pi
numerator = 5 * mp.pi

# Calculate denominator: 4 * sqrt(2)
denominator = 4 * mp.sqrt(2)

# Compute the result: numerator / denominator
result = numerator / denominator

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))