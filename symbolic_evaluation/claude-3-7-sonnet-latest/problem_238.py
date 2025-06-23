import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define the numerator and denominator
numerator = 8
denominator = 3

# Compute the fraction 8/3 using high-precision arithmetic
result = mp.mpf(numerator) / mp.mpf(denominator)

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))