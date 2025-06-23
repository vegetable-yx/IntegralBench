import mpmath as mp

mp.dps = 15

# Compute Bessel function of the first kind J0 at 1
bessel_j0_1 = mp.besselj(0, 1)

# Multiply by π to get the final result
result = mp.pi * bessel_j0_1

print(mp.nstr(result, n=10))