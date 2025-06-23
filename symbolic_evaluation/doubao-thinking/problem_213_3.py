import mpmath as mp

# Set internal decimal precision to 15 for accurate 10-digit output
mp.dps = 15

# Compute the Bessel function of the first kind of order 0 at 1
bessel_value = mp.besselj(0, 1)

# Multiply the Bessel function result by pi
result = mp.pi * bessel_value

# Print the final result to exactly 10 decimal places
print(mp.nstr(result, n=10))