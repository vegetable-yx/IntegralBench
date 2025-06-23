import mpmath as mp

# Set precision to 15 decimal places for calculations
mp.dps = 15

# Calculate square root of 2
sqrt2 = mp.sqrt(2)

# Calculate modified Bessel function of the first kind of order 0 at 1
i0 = mp.besseli(0, 1)

# Multiply components together with pi
result = sqrt2 * mp.pi * i0

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))