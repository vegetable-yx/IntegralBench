import mpmath as mp
mp.dps = 15

# Calculate numerator and denominator
numerator = mp.mpf(2)
denominator = mp.mpf(9)

# Compute the exact fraction
result = numerator / denominator

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))