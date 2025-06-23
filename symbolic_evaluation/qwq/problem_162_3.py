import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate square root of 2
sqrt2 = mp.sqrt(2)

# Calculate modified Bessel function of first kind I_0(1)
bessel_term = mp.besseli(0, 1)

# Multiply components together: π * sqrt(2) * I_0(1)
result = mp.pi * sqrt2 * bessel_term

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))