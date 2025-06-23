import mpmath as mp
mp.dps = 15

# Compute the modified Bessel function of the first kind I_0(6)
i0_value = mp.besseli(0, 6)

# Subtract 1 from the Bessel function result
result = i0_value - 1

print(mp.nstr(result, n=10))