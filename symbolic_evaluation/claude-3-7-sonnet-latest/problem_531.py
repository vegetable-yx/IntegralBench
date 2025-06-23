import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define the numerator and denominator for the fraction
numerator = -179
denominator = 32

# Compute the exact fraction using mpmath
result = mp.mpf(numerator) / mp.mpf(denominator)

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))