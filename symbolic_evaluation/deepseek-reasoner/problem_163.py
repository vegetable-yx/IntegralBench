import mpmath as mp
mp.dps = 15

# Calculate numerator and denominator
numerator = 1664
denominator = 27

# Perform exact division using mpmath
result = mp.mpf(numerator) / mp.mpf(denominator)

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))