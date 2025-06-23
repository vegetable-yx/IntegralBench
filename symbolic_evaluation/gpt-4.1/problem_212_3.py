import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Calculate Bessel functions at x=1
# J0(1): Bessel function of the first kind of order 0 at 1
bessel_j0 = mp.besselj(0, 1)

# J2(1): Bessel function of the first kind of order 2 at 1
bessel_j2 = mp.besselj(2, 1)

# Compute the difference: J0(1) - J2(1)
diff = bessel_j0 - bessel_j2

# Multiply by pi/2
result = (mp.pi / 2) * diff

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))