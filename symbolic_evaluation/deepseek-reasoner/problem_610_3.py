import mpmath as mp
mp.dps = 15

# Direct assignment of the analytical result
result = mp.mpf(1)

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))