import mpmath as mp

# Set precision to 15 decimal places for calculations
mp.dps = 15

# Calculate square root of pi
sqrt_pi = mp.sqrt(mp.pi)

# Calculate modified Bessel function of the first kind of order 0 at 1
i0 = mp.besseli(0, 1)

# Combine components to get final result
result = 2 * sqrt_pi * i0

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))