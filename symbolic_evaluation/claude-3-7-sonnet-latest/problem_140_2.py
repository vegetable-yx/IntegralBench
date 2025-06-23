import mpmath as mp

# Set internal decimal precision to 15 for intermediate calculations
mp.dps = 15

# Compute the modified Bessel function of the first kind of order 1 at z=1
bessel_value = mp.besseli(1, 1)

# Square the Bessel function value
bessel_squared = bessel_value**2

# Multiply by 2*pi
result = 2 * mp.pi * bessel_squared

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))