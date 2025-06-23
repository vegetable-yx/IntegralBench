import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Compute the Bessel function of the first kind J0 at 1
bessel_value = mp.besselj(0, 1)

# Multiply by π to get the final result
result = mp.pi * bessel_value

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))