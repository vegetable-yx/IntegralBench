import mpmath as mp
mp.dps = 15  # Direct assignment of constant value
result = mp.mpf(2)

print(mp.nstr(result, n=10))