import mpmath as mp

# Set the decimal places for internal precision
mp.dps = 15

# Compute the fraction 5/6
numerator = 5
denominator = 6
result = mp.mpf(numerator) / mp.mpf(denominator)

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))