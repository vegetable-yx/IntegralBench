import mpmath as mp
mp.dps = 15

# Calculate numerator and denominator
numerator = 253
denominator = 3

# Compute the fraction 253/3 with high precision
fraction = mp.mpf(numerator) / mp.mpf(denominator)

# Calculate natural logarithm of the fraction
result = mp.log(fraction)

# Print result with 10 decimal places
print(mp.nstr(result, n=10))