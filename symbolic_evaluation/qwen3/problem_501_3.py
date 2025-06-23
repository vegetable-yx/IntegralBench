import mpmath as mp
mp.dps = 15

# Calculate numerator and denominator
numerator = mp.mpf(2)
denominator = mp.mpf(5)

# Compute the simple fraction
result = numerator / denominator

# Print result with 10 decimal places
print(mp.nstr(result, n=10))