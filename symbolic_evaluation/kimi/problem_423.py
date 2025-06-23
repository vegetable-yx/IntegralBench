import mpmath as mp
mp.dps = 15

# Direct assignment of the exact solution
result = mp.mpf(99)

# Print result with 10 decimal places
print(mp.nstr(result, n=10))