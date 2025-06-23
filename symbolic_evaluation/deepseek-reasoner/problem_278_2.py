import mpmath as mp
mp.dps = 15

# Calculate modified Bessel function of first kind order 0 at 1
i0_value = mp.besseli(0, 1)

# Multiply by π to get final result
result = mp.pi * i0_value

print(mp.nstr(result, n=10))