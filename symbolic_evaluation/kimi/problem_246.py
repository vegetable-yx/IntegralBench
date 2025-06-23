import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Calculate numerator and denominator
numerator = mp.mpf(3)
denominator = mp.mpf(320)

# Compute the final result
result = numerator / denominator

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))