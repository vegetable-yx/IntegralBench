import mpmath as mp
mp.dps = 15  # Set decimal precision for all calculations

# Calculate Bessel function of the first kind J0(1)
bessel_value = mp.besselj(0, 1)

# Compute the difference from 1
difference = bessel_value - 1

# Multiply by π/4 to get final result
result = (mp.pi / 4) * difference

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))