import mpmath as mp
mp.dps = 15

# Direct assignment of the exact solution
result = mp.mpf(1)

# Print result with 10 decimal place precision
print(mp.nstr(result, n=10))