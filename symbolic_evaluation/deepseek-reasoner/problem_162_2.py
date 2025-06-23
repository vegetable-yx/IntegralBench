import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate components of the expression sqrt(2) * pi * I_0(1)
sqrt2 = mp.sqrt(2)  # Compute square root of 2
pi = mp.pi          # Get pi constant
i0 = mp.besseli(0, 1)  # Compute modified Bessel function of first kind (order 0 at 1)

# Combine components into final result
result = sqrt2 * pi * i0

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))