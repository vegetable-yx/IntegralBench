import mpmath as mp
mp.dps = 15

# Compute the Bessel function of the first kind J_0(2)
bessel_value = mp.besselj(0, 2)

# Multiply by 1/4 to get the final result
result = bessel_value * mp.mpf(1)/4

print(mp.nstr(result, n=10))