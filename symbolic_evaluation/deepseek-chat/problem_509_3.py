import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the numerator: 8 * pi
numerator = 8 * mp.pi

# Divide by 3 to get the final result
result = numerator / 3

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))