import mpmath as mp
mp.dps = 15

# Direct assignment of zero result
result = mp.mpf(0)

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))