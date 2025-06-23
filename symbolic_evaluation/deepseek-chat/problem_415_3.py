import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute the fraction 4/5
numerator = 4
denominator = 5
result = mp.mpf(numerator) / mp.mpf(denominator)

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))