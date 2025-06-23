import mpmath as mp

# Set internal decimal precision to 15 digits
mp.dps = 15

# Calculate the constant pi/8
pi_over_8 = mp.pi / 8

# Compute the Bessel function of the first kind J0(2)
bessel_j0_2 = mp.besselj(0, 2)

# Multiply to get the final result: (pi/8) * J0(2)
result = pi_over_8 * bessel_j0_2

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))