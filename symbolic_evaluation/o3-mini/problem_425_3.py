import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Assign numerator and denominator values
numerator = 128
denominator = 153

# Compute the fraction using high-precision arithmetic
result = mp.mpf(numerator) / mp.mpf(denominator)

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))