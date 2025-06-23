import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Calculate the numerator (3 * π)
numerator = mp.mpf(3) * mp.pi

# Calculate the denominator (16)
denominator = mp.mpf(16)

# Compute the final result
result = numerator / denominator

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))