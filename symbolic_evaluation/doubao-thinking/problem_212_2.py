import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate Bessel functions of the first kind at x=1
J0_1 = mp.besselj(0, 1)  # J_0(1)
J2_1 = mp.besselj(2, 1)  # J_2(1)

# Compute the difference between Bessel functions
bessel_diff = J0_1 - J2_1

# Multiply by π/2 to get final result
result = (mp.pi / 2) * bessel_diff

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))