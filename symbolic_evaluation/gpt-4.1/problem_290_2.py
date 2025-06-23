import mpmath as mp
mp.dps = 15

# Calculate the simple fraction using high-precision arithmetic
result = mp.mpf(1)/2

# Print result with 10 decimal places
print(mp.nstr(result, n=10))