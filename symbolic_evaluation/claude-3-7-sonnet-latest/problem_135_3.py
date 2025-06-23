import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the numerator: 3 * pi
numerator = 3 * mp.pi

# Divide by 4 to get the result
result = numerator / 4

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))