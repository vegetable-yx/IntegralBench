import mpmath as mp
mp.dps = 15

# Calculate numerator and denominator as mpmath floats
numerator = mp.mpf(253)
denominator = mp.mpf(3)

# Compute the fraction 253_over_3 = 253/3
fraction = numerator / denominator

# Calculate natural logarithm of the fraction
result = mp.log(fraction)

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))