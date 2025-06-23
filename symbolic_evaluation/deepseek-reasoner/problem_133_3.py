import mpmath as mp
mp.dps = 15

# The analytical result is simply 2
result = mp.mpf(2)

print(mp.nstr(result, n=10))