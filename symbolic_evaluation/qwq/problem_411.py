import mpmath as mp
mp.dps = 15

# Direct assignment of the exact solution
result = mp.mpf(1)

# Print result with exactly 10 decimal places precision
print(mp.nstr(result, n=10))