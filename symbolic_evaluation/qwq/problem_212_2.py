import mpmath as mp

mp.dps = 15  # Set decimal precision for calculations

# Compute Bessel functions of the first kind at x=1
J0 = mp.besselj(0, 1)  # J_0(1)
J2 = mp.besselj(2, 1)  # J_2(1)

# Calculate the difference between Bessel functions
bessel_diff = J0 - J2

# Multiply by pi/2 to get final result
result = (mp.pi / 2) * bessel_diff

print(mp.nstr(result, n=10))