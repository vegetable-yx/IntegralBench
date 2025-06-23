import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate components of the expression sqrt(3) * pi * I_0(3)
sqrt3 = mp.sqrt(3)          # Compute square root of 3
bessel_i0 = mp.besseli(0, 3)  # Compute modified Bessel function of first kind I_0(3)

# Combine components to get final result
result = sqrt3 * mp.pi * bessel_i0

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))