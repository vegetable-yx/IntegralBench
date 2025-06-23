import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define the numerator and denominator
numerator = 5
denominator = 8

# Compute the fraction using exact mpmath operations
result = mp.mpf(numerator) / mp.mpf(denominator)

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))