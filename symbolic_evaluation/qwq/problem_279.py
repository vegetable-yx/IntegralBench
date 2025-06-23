import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Calculate modified Bessel function of first kind, order 0 at z=1
bessel_term = mp.besseli(0, 1)

# Multiply by π to get final result
result = mp.pi * bessel_term

print(mp.nstr(result, n=10))