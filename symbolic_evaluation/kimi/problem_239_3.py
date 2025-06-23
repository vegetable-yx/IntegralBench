import mpmath as mp
mp.dps = 15

# Compute modified Bessel function of the second kind K_1(2)
result = mp.besselk(1, 2)

print(mp.nstr(result, n=10))