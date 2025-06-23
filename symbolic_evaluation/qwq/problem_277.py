import mpmath as mp

# Set the internal precision to 15 decimal places
mp.dps = 15

# Calculate modified Bessel functions of the first kind
i0 = mp.besseli(0, 1)  # I_0(1)
i1 = mp.besseli(1, 1)  # I_1(1)

# Compute the difference between Bessel functions
bessel_diff = i0 - i1

# Multiply by pi to get the final result
result = mp.pi * bessel_diff

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))