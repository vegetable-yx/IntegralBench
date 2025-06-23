import mpmath as mp
mp.dps = 15  # Set internal precision

# Calculate numerator and denominator
numerator = mp.mpf(1)
denominator = mp.mpf(128)

# Compute the exact fraction
result = numerator / denominator

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))