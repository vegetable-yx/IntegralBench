import mpmath as mp

# Set internal decimal places for high precision calculation
mp.dps = 15

# Calculate numerator: 4 minus pi
numerator = 4 - mp.pi

# Divide numerator by 2 to get the result
result = numerator / 2

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))