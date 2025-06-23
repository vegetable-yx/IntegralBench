import mpmath as mp
mp.dps = 15

# Calculate numerator and denominator using high precision
numerator = mp.mpf(4)
denominator = mp.mpf(5)

# Perform exact division operation
result = numerator / denominator

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))