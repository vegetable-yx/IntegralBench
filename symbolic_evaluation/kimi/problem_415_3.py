import mpmath as mp
mp.dps = 15

# Calculate numerator and denominator
numerator = mp.mpf(4)
denominator = mp.mpf(5)

# Compute the division
result = numerator / denominator

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))