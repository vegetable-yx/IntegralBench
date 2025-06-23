import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute Bessel function of the first kind of order 0 at x=1
bessel_val = mp.besselj(0, 1)

# Multiply by pi to get the result
result = mp.pi * bessel_val

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))