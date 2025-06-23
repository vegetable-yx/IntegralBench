import mpmath as mp
mp.dps = 15

# The analytical result is exactly 0
result = mp.mpf(0)

print(mp.nstr(result, n=10))