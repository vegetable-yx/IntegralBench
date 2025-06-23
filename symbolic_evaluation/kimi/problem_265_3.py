import mpmath as mp

# Set decimal places for internal calculations
mp.dps = 15

# Calculate Bessel function of the first kind, order 0 at 2
j0_val = mp.besselj(0, 2)

# Calculate Bessel function of the first kind, order 2 at 2
j2_val = mp.besselj(2, 2)

# Compute the difference: J0(2) - J2(2)
bessel_diff = j0_val - j2_val

# Multiply by pi/4 to get the final result
result = (mp.pi / 4) * bessel_diff

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))