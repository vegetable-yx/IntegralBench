import mpmath as mp
mp.dps = 15

# Calculate the simple fraction 1/2 using arbitrary precision
numerator = 1
denominator = 2
result = mp.mpf(numerator) / mp.mpf(denominator)

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))