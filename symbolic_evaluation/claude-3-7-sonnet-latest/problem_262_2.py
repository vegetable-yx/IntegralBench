import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute pi/8
pi_over_8 = mp.pi / 8

# Compute Bessel function J0(2)
bessel_j0_at_2 = mp.besselj(0, 2)

# Multiply to get (pi/8) * J0(2)
product = pi_over_8 * bessel_j0_at_2

# Subtract 1/4 from the product
result = product - 0.25

# Print the final result to 10 decimal places
print(mp.nstr(result, n=10))