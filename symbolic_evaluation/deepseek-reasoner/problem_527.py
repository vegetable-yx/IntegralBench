import mpmath as mp
mp.dps = 15  # The analytical result is exactly zero
result = mp.mpf(0)  # Direct assignment of zero value with mpmath precision

print(mp.nstr(result, n=10))