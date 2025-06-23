import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate sqrt(pi/2)
sqrt_pi_over_2 = mp.sqrt(mp.pi / 2)

# Calculate modified Bessel function of first kind I_0(3)
bessel_i0_3 = mp.besseli(0, 3)

# Multiply components to get final result
result = sqrt_pi_over_2 * bessel_i0_3

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))