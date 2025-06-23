import mpmath as mp
mp.dps = 15
result = mp.pi
print(mp.nstr(result, n=10))