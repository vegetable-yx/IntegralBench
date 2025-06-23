import mpmath as mp
mp.dps = 15  # Calculate Bessel function of the first kind of order 1 at 1
bessel_value = mp.besselj(1, 1)

# Multiply by pi to get the final result
result = mp.pi * bessel_value

# Print the result with 10 decimal precision
print(mp.nstr(result, n=10))