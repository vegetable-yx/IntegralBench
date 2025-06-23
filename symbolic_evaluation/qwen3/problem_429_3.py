import mpmath as mp
mp.dps = 15

# Calculate numerator and denominator as high-precision floats
numerator = mp.mpf(80)
denominator = mp.mpf(23)

# Compute the fraction 80/23 with full precision
fraction = numerator / denominator

# Calculate natural logarithm of the fraction
result = mp.log(fraction)

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))