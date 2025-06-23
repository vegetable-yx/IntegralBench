import mpmath as mp
mp.dps = 15  # Set internal decimal precision

# Compute the Bessel function of the first kind J0 at z=1
bessel_term = mp.besselj(0, 1)

# Multiply by π to get the final result
result = mp.pi * bessel_term

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))