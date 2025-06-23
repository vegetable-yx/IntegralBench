import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Calculate Bessel functions of the first kind
j0 = mp.besselj(0, 1)  # J_0(1)
j2 = mp.besselj(2, 1)  # J_2(1)

# Compute the difference between Bessel functions
bessel_diff = j0 - j2

# Multiply by π/2 to get final result
result = (mp.pi / 2) * bessel_diff

# Print result with 10 decimal places
print(mp.nstr(result, n=10))