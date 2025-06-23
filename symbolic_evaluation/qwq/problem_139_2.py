import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Calculate the (π - 2) term
pi_minus_2 = mp.pi - 2

# Compute the modified Bessel function of the first kind I_0(2)
bessel_i0_2 = mp.besseli(0, 2)

# Multiply components to get final result
result = pi_minus_2 * bessel_i0_2

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))