import mpmath as mp

# Set internal decimal places to 15 for sufficient precision
mp.dps = 15

# Compute the modified Bessel function of the first kind of order 1 at 2
bessel_val = mp.besseli(1, 2)

# Multiply the Bessel function result by 2
result = 2 * bessel_val

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))