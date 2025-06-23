import mpmath as mp

# Set internal decimal precision to 15 to ensure accuracy
mp.dps = 15

# Compute Bessel functions of the first kind at x=1
# J0(1) - Bessel function of order 0 at 1
bessel_j0 = mp.besselj(0, 1)

# J1(1) - Bessel function of order 1 at 1
bessel_j1 = mp.besselj(1, 1)

# J2(1) - Bessel function of order 2 at 1
bessel_j2 = mp.besselj(2, 1)

# Compute the expression: π * (J0(1) + J2(1)) - 2 * J1(1)
term1 = mp.pi * (bessel_j0 + bessel_j2)
term2 = 2 * bessel_j1
result = term1 - term2

# Print the result formatted to 10 decimal places
print(mp.nstr(result, n=10))