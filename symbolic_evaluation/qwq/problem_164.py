import mpmath as mp
mp.dps = 15

# Direct assignment of the exact integer value
result = mp.mpf(384)

# Print result with 10 decimal place precision
print(mp.nstr(result, n=10))