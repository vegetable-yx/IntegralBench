import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute Bessel function of the first kind of order 1 at x=1
bessel_val = mp.besselj(1, 1)

# Multiply the result by pi
result = mp.pi * bessel_val

# Print the final result with 10 decimal places
print(mp.nstr(result, n=10))