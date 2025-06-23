import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate modified Bessel functions of the first kind
i0 = mp.besseli(0, 1)  # I_0(1)
i2 = mp.besseli(2, 1)  # I_2(1)

# Sum the Bessel function values
bessel_sum = i0 + i2

# Multiply by π/2 to get final result
result = (mp.pi / 2) * bessel_sum

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))