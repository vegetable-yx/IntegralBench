import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Calculate modified Bessel function of first kind order 0 at 1
bessel_value = mp.besseli(0, 1)

# Multiply by π to get final result
result = mp.pi * bessel_value

# Print result with 10 decimal place precision
print(mp.nstr(result, n=10))