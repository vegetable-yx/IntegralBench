import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate numerator and denominator separately
numerator = mp.mpf(4)
denominator = mp.pi  # Use mpmath's built-in pi constant

# Compute the final result
result = numerator / denominator

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))