import mpmath as mp
mp.dps = 15  # Set internal precision

# Calculate the simple fraction 1/4 using high-precision arithmetic
numerator = 1
denominator = 4
result = mp.mpf(numerator) / mp.mpf(denominator)

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))