import mpmath as mp
mp.dps = 15

# Direct assignment of the constant value
result = mp.mpf(1)

print(mp.nstr(result, n=10))