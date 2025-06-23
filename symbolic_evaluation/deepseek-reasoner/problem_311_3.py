import mpmath as mp
mp.dps = 15

# Calculate numerator and denominator
numerator = 1
denominator = 4

# Compute the fraction using high-precision arithmetic
result = mp.mpf(numerator) / mp.mpf(denominator)

# Print result with 10 decimal places
print(mp.nstr(result, n=10))