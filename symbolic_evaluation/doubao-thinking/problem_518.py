import mpmath as mp
mp.dps = 15  # Direct assignment of the exact integer value
result = mp.mpf(4036)

print(mp.nstr(result, n=10))