import mpmath as mp
mp.dps = 15
result = mp.mpf(113)
print(mp.nstr(result, n=10))