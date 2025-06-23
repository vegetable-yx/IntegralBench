import mpmath as mp

mp.dps = 15

# Calculate numerator and denominator as high-precision floats
numerator = mp.mpf(2023)
denominator = mp.mpf(2022)

# Compute the exact fraction
result = -numerator / denominator

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))