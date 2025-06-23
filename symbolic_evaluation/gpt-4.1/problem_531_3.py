import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Define numerator and denominator
numerator = 5
denominator = 6

# Compute the fraction
result = mp.mpf(numerator) / mp.mpf(denominator)

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))