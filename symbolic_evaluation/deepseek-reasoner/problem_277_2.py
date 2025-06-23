import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate modified Bessel functions of the first kind
i0 = mp.besseli(0, 1)  # I_0(1)
i1 = mp.besseli(1, 1)  # I_1(1)

# Compute the difference between Bessel functions
bessel_diff = i0 - b1

# Multiply by π to get final result
result = mp.pi * bessel_diff

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))