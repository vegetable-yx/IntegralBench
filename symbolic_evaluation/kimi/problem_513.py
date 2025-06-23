import mpmath as mp
mp.dps = 15

# Direct assignment of the result from analytical solution
result = mp.mpf(0)

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))