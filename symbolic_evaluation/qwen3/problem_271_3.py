import mpmath as mp

mp.dps = 15  # Set decimal precision for calculations

# Calculate the numerator (19 * π)
numerator = 19 * mp.pi

# Compute the final result by dividing by 512
result = numerator / 512

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))