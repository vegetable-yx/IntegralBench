import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the numerator: 4 times pi
numerator = 4 * mp.pi

# Compute the final result: numerator divided by 3
result = numerator / 3

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))