import mpmath as mp

# Set internal decimal places for high precision calculation
mp.dps = 15

# Define numerator and denominator
numerator = 8
denominator = 7

# Compute the fraction using mpmath for exact precision
result = mp.mpf(numerator) / mp.mpf(denominator)

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))