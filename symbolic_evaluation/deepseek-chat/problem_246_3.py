import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Numerator and denominator of the fraction
numerator = 3465
denominator = 8

# Compute the exact value of the fraction
result = mp.mpf(numerator) / mp.mpf(denominator)

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))