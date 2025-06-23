import mpmath as mp
mp.dps = 15

# Compute Bessel function of the first kind J0(1)
bessel_j0 = mp.besselj(0, 1)

# Multiply by π to scale the Bessel function result
pi_scaled = mp.pi * bessel_j0

# Multiply by √2 to complete the original expression
result = mp.sqrt(2) * pi_scaled

print(mp.nstr(result, n=10))