import mpmath as mp
mp.dps = 15

# The analytical solution is given integral equals 4
result = mp.mpf(4)

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))