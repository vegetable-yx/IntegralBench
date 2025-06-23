import mpmath as mp

# Set the internal decimal precision to 15 digits
mp.dps = 15

# Compute the modified Bessel function of the first kind of order 0 at z=1
bessel_val = mp.besseli(0, 1)

# Multiply by pi to get the final result
result = mp.pi * bessel_val

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))