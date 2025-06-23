import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate square root of 3
sqrt3 = mp.sqrt(3)

# Get mathematical constant pi
pi = mp.pi

# Compute modified Bessel function of first kind (order 0) at 3
bessel_i0_3 = mp.besseli(0, 3)

# Combine components to get final result
result = sqrt3 * pi * bessel_i0_3

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))