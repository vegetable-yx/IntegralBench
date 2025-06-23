import mpmath as mp
mp.dps = 15

# Calculate sqrt(3)
sqrt3 = mp.sqrt(3)

# Compute numerator (2 + sqrt(3))
numerator = 2 + sqrt3

# Compute the fraction (2 + sqrt(3)) / sqrt(3)
fraction = numerator / sqrt3

# Calculate natural logarithm of the fraction
result = mp.log(fraction)

# Print result to 10 decimal places
print(mp.nstr(result, n=10))