import mpmath as mp
mp.dps = 15

# Calculate numerator and denominator using high-precision floats
numerator = mp.mpf(5)
denominator = mp.mpf(2)

# Perform exact division
result = numerator / denominator

# Print result with 10 decimal places
print(mp.nstr(result, n=10))