import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Compute the Bessel function of the first kind of order 0 at z=1
bessel_term = mp.besselj(0, 1)

# Multiply by pi constant
result = mp.pi * bessel_term

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))