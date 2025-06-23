import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate the square root of 3
sqrt3 = mp.sqrt(3)

# Compute the coefficient (π * sqrt(3)) / 2
pi_sqrt3_over_2 = (mp.pi * sqrt3) / 2

# Calculate the modified Bessel function of the first kind I_0(3)
bessel_i0 = mp.besseli(0, 3)

# Multiply components to get final result
result = pi_sqrt3_over_2 * bessel_i0

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))