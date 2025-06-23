import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define numerator and denominator
numerator = 1
denominator = 5

# Compute the exact fraction value
result = mp.mpf(numerator) / mp.mpf(denominator)

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))