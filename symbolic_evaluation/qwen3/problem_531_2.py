import mpmath as mp
mp.dps = 15

# Calculate numerator and denominator
numerator = 5
denominator = 6

# Compute the exact fraction using arbitrary precision
result = mp.mpf(numerator) / mp.mpf(denominator)

# Print result with 10 decimal places
print(mp.nstr(result, n=10))