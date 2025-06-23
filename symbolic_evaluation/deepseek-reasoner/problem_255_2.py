import mpmath as mp
mp.dps = 15
result = -3 * mp.pi
print(mp.nstr(result, n=10))