import mpmath as mp

# Set the internal precision to 15 decimal places
mp.dps = 15

# Calculate the modified Bessel function of the first kind of order 0 at 3
bessel_val = mp.besseli(0, 3)

# Compute the constant factor: (3 * sqrt(3)) / 2
factor = (3 * mp.sqrt(3)) / 2

# Multiply the factor by pi
factor_pi = factor * mp.pi

# Multiply by the Bessel function value to get the final result
result = factor_pi * bessel_val

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))