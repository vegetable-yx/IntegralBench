import mpmath as mp
mp.dps = 15  # Assign exact value directly
result = mp.mpf(1)
print(mp.nstr(result, n=10))