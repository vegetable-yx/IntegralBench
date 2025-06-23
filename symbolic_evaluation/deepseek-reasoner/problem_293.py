import mpmath as mp
mp.dps = 15

# Direct assignment of the analytical result
result = mp.mpf(4)

print(mp.nstr(result, n=10))