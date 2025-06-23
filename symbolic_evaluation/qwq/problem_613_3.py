import mpmath as mp
mp.dps = 15

# Calculate numerator and denominator using high precision
numerator = mp.mpf(1)
denominator = mp.mpf(5)

# Compute the exact fraction division
result = numerator / denominator

# Print result with 10 decimal places
print(mp.nstr(result, n=10))