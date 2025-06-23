import mpmath as mp

# Set precision to 15 decimal places for calculations
mp.dps = 15

# Calculate π/2
pi_over_2 = mp.pi / 2

# Calculate the modified Bessel function of first kind I_0(1)
bessel_i0 = mp.besseli(0, 1)

# Multiply components to get final result
result = pi_over_2 * bessel_i0

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))