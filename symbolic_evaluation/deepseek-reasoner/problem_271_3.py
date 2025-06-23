import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate numerator and denominator
numerator = 83
denominator = 512

# Compute the coefficient fraction
coefficient = mp.mpf(numerator) / mp.mpf(denominator)

# Multiply by pi to get final result
result = coefficient * mp.pi

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))