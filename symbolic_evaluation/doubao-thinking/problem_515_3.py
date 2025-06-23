import mpmath as mp
mp.dps = 15

# The analytical solution is a simple constant value
result = mp.mpf(1)

print(mp.nstr(result, n=10))