import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Compute the modified Bessel function of the first kind of order 1/4 at z=3
bessel_val = mp.besseli(0.25, 3)

# Compute the constant sqrt(3 * pi)
sqrt_const = mp.sqrt(3 * mp.pi)

# Multiply the two components
result = sqrt_const * bessel_val

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))