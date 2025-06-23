import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places
result = mp.mpf(1)  # Direct assignment of analytical result
print(mp.nstr(result, n=10))