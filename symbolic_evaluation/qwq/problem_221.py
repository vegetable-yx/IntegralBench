import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate the numerator (3 * π)
numerator = 3 * mp.pi

# Divide by 16 to get the final result
result = numerator / 16

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))