import mpmath as mp
mp.dps = 15

# Calculate numerator and denominator using arbitrary precision
numerator = mp.mpf(1)
denominator = mp.mpf(9)

# Perform exact division with high precision
result = numerator / denominator

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))