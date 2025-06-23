import mpmath as mp

mp.dps = 15

# Calculate numerator and denominator
numerator = 80
denominator = 23

# Compute the ratio of numerator to denominator
ratio = mp.mpf(numerator) / mp.mpf(denominator)

# Calculate natural logarithm of the ratio
result = mp.log(ratio)

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))