import mpmath as mp
mp.dps = 15

# Calculate numerator and denominator as arbitrary-precision floats
numerator = mp.mpf(1)
denominator = mp.mpf(12)

# Perform exact rational division with mpmath precision
result = numerator / denominator

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))