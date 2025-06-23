import mpmath as mp
mp.dps = 15  # Set internal decimal precision

# Compute Bessel functions of the first kind at order 0 and 2
j0 = mp.besselj(0, 1)  # J₀(1)
j2 = mp.besselj(2, 1)  # J₂(1)

# Calculate the difference between Bessel functions
bessel_diff = j0 - j2

# Multiply by π/2 to get final result
result = (mp.pi / 2) * bessel_diff

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))