import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Calculate the numerator: 2 * sqrt(2) - 3
numerator = 2 * mp.sqrt(2) - 3

# Divide the numerator by 8 to get the result
result = numerator / 8

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))