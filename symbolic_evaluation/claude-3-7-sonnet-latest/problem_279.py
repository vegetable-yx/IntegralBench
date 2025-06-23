import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Compute the modified Bessel function of the first kind of order 0 at z=1
bessel_value = mp.besseli(0, 1)

# Multiply by pi to get the final result
result = mp.pi * bessel_value

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))