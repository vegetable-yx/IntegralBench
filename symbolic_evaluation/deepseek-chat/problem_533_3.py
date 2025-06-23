import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define numerator and denominator
numerator = 8
denominator = 7

# Compute the fraction: 8/7
result = mp.mpf(numerator) / mp.mpf(denominator)

# Print result to exactly 10 decimal places
print(mp.nstr(result, n=10))