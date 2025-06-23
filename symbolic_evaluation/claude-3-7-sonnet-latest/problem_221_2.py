import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the numerator: 49 * pi
numerator = 49 * mp.pi

# Divide by 8 to get the final result
result = numerator / 8

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))