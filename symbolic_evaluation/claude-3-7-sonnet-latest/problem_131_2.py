import mpmath as mp

# Set internal decimal places for precision
mp.dps = 15

# Compute the modified Bessel function of the first kind at order 1 for argument 2
bessel_term = mp.besseli(1, 2)

# Multiply by 4*pi to get the result
result = 4 * mp.pi * bessel_term

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))