import mpmath as mp
mp.dps = 15

# Calculate numerator and denominator separately
numerator = mp.mpf(4)
denominator = mp.pi

# Compute the final result
result = numerator / denominator

# Print with 10 decimal precision
print(mp.nstr(result, n=10))