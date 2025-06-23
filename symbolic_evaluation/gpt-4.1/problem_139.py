import mpmath as mp

# Set internal decimal precision to 15 for accurate computation
mp.dps = 15

# Compute the modified Bessel function of the first kind of order 1 at 2
bessel_value = mp.besseli(1, 2)

# Multiply the result by 2 as per the analytical expression
result = 2 * bessel_value

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))