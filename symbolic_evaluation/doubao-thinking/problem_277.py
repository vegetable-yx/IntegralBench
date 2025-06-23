import mpmath as mp

# Set precision to 15 decimal places for calculations
mp.dps = 15

# Calculate modified Bessel functions of the first kind
i0 = mp.besseli(0, 1)  # I_0(1)
i1 = mp.besseli(1, 1)  # I_1(1)

# Compute the difference between Bessel functions
difference = i0 - i1

# Multiply by pi to get final result
result = mp.pi * difference

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))