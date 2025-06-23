import mpmath as mp
mp.dps = 15

# Compute modified Bessel function of first kind order 0 at 1
i0 = mp.besseli(0, 1)

# Multiply by pi to get the integral result
result = mp.pi * i0

print(mp.nstr(result, n=10))