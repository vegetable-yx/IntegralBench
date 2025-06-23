import mpmath as mp
mp.dps = 15

# Calculate the simple fraction using exact rational arithmetic
numerator = mp.mpf(1)
denominator = mp.mpf(24)
result = numerator / denominator

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))