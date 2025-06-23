import mpmath as mp

# Set internal decimal precision to 15 for intermediate calculations
mp.dps = 15

# Compute the constant factor: π/2
pi_over_2 = mp.pi / 2

# Compute the Bessel function of the first kind of order 0 at z=1
bessel_j0_at_1 = mp.besselj(0, 1)

# Multiply the constant factor by the Bessel function value
result = pi_over_2 * bessel_j0_at_1

# Print the final result rounded to 10 decimal places
print(mp.nstr(result, n=10))