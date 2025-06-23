import mpmath as mp

mp.dps = 15  # Set internal precision for calculations

# Compute modified Bessel function of first kind, order 0 at 1
bessel_term = mp.besseli(0, 1)

# Multiply by pi to get the final result
result = mp.pi * bessel_term

# Print result with 10 decimal places using mpmath's nstr
print(mp.nstr(result, n=10))