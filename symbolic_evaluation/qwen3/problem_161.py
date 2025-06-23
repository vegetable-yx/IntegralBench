import mpmath as mp
mp.dps = 15

# Compute modified Bessel functions of the first kind
i0 = mp.besseli(0, 1)  # I_0(1)
i1 = mp.besseli(1, 1)  # I_1(1)

# Calculate the difference between Bessel functions
bessel_diff = i0 - i1

# Multiply by sqrt(2) and pi
result = mp.sqrt(2) * mp.pi * bessel_diff

print(mp.nstr(result, n=10))