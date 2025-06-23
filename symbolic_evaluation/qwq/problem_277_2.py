import mpmath as mp

# Set the internal precision to 15 decimal places
mp.dps = 15

# Calculate modified Bessel functions of the first kind
i0 = mp.besseli(0, 1)  # I_0(1)
i2 = mp.besseli(2, 1)  # I_2(1)

# Sum the Bessel function values
bessel_sum = i0 + i2

# Multiply by pi to get the final result
result = mp.pi * bessel_sum

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))