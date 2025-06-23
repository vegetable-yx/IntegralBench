import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define numerator and denominator
numerator = -31
denominator = 6

# Compute the result by dividing numerator by denominator
result = mp.mpf(numerator) / mp.mpf(denominator)

# Print the result to 10 significant digits
print(mp.nstr(result, n=10))