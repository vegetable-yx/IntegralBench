import mpmath as mp
mp.dps = 15

# Compute Bessel function of the first kind of order 0 at 1
bessel_term = mp.besselj(0, 1)

# Multiply by π to get the final integral value
result = mp.pi * bessel_term

print(mp.nstr(result, n=10))