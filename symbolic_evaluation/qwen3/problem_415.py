import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate numerator and denominator
numerator = mp.mpf(4)
denominator = mp.mpf(5)

# Compute the exact fraction
result = numerator / denominator

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))