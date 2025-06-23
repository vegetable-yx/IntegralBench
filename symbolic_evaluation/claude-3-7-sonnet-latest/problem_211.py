import mpmath as mp

# Set internal decimal precision to 15 for intermediate calculations
mp.dps = 15

# Compute pi constant
pi_val = mp.pi

# Calculate the Bessel function of the first kind of order 0 at z=2
bessel_j0 = mp.besselj(0, 2)

# Multiply by pi/2 to get the final result
result = (pi_val / 2) * bessel_j0

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))