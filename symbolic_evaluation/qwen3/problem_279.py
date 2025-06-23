import mpmath as mp
mp.dps = 15

# Calculate modified Bessel function of the first kind of order 0 at 1
i0 = mp.besseli(0, 1)

# Multiply by pi to get the final result
result = mp.pi * i0

print(mp.nstr(result, n=10))