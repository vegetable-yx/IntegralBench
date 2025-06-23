import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Define the numerator and denominator
numerator = 8
denominator = 7

# Compute the fraction using mpmath
result = mp.mpf(numerator) / mp.mpf(denominator)

# Output the result with exactly 10 decimal places
print(mp.nstr(result, n=10))