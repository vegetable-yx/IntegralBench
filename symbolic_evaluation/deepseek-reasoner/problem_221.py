import mpmath as mp

# Set the internal precision to 15 decimal places
mp.dps = 15

# Calculate the numerator (3 * π)
numerator = mp.mpf(3) * mp.pi

# Calculate the denominator (16)
denominator = mp.mpf(16)

# Compute the final result (3π/16)
result = numerator / denominator

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))