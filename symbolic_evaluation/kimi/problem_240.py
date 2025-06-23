import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate numerator: 2 * sqrt(2) - 3
numerator = 2 * mp.sqrt(2) - 3

# Divide by 8 to get the final result
result = numerator / 8

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))