import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Calculate numerator and denominator
numerator = mp.mpf(27)
denominator = mp.mpf(8)

# Compute the exact fraction
result = numerator / denominator

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))