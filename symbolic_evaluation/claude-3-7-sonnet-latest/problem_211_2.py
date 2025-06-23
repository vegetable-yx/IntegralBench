import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the Bessel function of the first kind of order 0 at 2
bessel_value = mp.besselj(0, 2)

# Compute the constant factor pi/2
pi_over_2 = mp.pi / 2

# Multiply to get the final result: (pi/2) * J_0(2)
result = pi_over_2 * bessel_value

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))