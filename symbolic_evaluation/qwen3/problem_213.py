import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Calculate Bessel function of the first kind of order 0 at 1
bessel_j0_1 = mp.besselj(0, 1)

# Multiply by pi to get the final result
result = mp.pi * bessel_j0_1

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))