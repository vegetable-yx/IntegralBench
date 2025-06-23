import mpmath as mp
mp.dps = 15  # Set decimal places for internal calculations

# Calculate numerator and denominator
numerator = mp.mpf(1)
denominator = mp.mpf(8)

# Compute the final result
result = -numerator / denominator

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))