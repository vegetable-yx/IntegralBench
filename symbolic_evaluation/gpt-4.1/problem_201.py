import mpmath as mp

# Set internal decimal places to 15 for sufficient precision
mp.dps = 15

# Compute the Bessel function of the first kind of order 1 at x=1
bessel_value = mp.besselj(1, 1)

# Multiply by pi to get the final result
result = mp.pi * bessel_value

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))