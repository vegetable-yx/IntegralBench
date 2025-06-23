import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Calculate numerator: 11 * sqrt(11)
sqrt_11 = mp.sqrt(11)
numerator = mp.mpf(11) * sqrt_11

# Calculate denominator
denominator = mp.mpf(18)

# Compute final result
result = numerator / denominator

# Print result with 10 decimal places
print(mp.nstr(result, n=10))