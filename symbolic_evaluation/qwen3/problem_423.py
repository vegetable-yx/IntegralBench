import mpmath as mp
mp.dps = 15  # Assign exact integer value
result = mp.mpf(99)

print(mp.nstr(result, n=10))