import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define the numerator and denominator as exact integers
numerator = 3465
denominator = 8

# Compute the exact fraction using arbitrary-precision arithmetic
result = mp.mpf(numerator) / mp.mpf(denominator)

# Output the result to exactly 10 decimal places
print(mp.nstr(result, n=10))