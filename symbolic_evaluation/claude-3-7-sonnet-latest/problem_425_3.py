import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define the numerator and denominator
numerator = 677
denominator = 510

# Compute the exact fraction using mpmath
result = mp.mpf(numerator) / mp.mpf(denominator)

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))