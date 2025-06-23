import mpmath as mp

# Set internal decimal precision to 15 for accurate computation
mp.dps = 15

# Compute the Bessel function of the first kind of order 1 at 2
bessel_value = mp.besselj(1, 2)

# Multiply by pi and divide by 8 to get the final result
result = (mp.pi * bessel_value) / 8

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))