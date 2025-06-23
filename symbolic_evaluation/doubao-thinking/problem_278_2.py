import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute pi constant
pi_val = mp.pi

# Compute modified Bessel function of the first kind of order 0 at z=1
bessel_val = mp.besseli(0, 1)

# Multiply pi and the Bessel function result
result = pi_val * bessel_val

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))