import mpmath as mp
mp.dps = 15

# The analytical result is a constant value
result = 4036

print(mp.nstr(result, n=10))