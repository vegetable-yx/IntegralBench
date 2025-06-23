import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate numerator and denominator separately
numerator = 16  # 16 in the numerator
denominator = mp.pi  # π from mpmath's constants

# Compute the final result
result = numerator / denominator

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))