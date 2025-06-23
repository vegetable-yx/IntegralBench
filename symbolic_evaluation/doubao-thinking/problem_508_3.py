import mpmath as mp
mp.dps = 15

# The analytical result is exactly 4
result = 4

print(mp.nstr(result, n=10))