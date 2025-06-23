import mpmath as mp

# Set internal decimal places of precision for calculations
mp.dps = 15

# Compute the Bessel function of the first kind of order 0 at 1
bessel_value = mp.besselj(0, 1)

# Multiply by pi to obtain the integral value
result = mp.pi * bessel_value

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))