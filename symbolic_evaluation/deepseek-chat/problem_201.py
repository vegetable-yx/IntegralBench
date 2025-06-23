import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Compute the Bessel function of the first kind of order 1 at z=1
bessel_value = mp.besselj(1, 1)

# Multiply the result by π
result = mp.pi * bessel_value

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))