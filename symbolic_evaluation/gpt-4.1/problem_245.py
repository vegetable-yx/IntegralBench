import mpmath as mp

# Set the internal precision to 15 decimal places
mp.dps = 15

# Define numerator and denominator
numerator = 2048
denominator = 225

# Compute the fraction
result = mp.mpf(numerator) / mp.mpf(denominator)

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))