import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the numerator: 3 * π
numerator = 3 * mp.pi

# Divide by 16 to get the final result
result = numerator / 16

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))