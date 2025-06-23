import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Compute modified Bessel function of the first kind of order 0 at 1
bessel_term = mp.besseli(0, 1)

# Multiply by π to get the final result
result = mp.pi * bessel_term

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))