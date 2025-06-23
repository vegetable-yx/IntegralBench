import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Compute modified Bessel functions of the first kind at x=1
i0 = mp.besseli(0, 1)  # I_0(1)
i2 = mp.besseli(2, 1)  # I_2(1)

# Calculate the difference between Bessel functions
bessel_diff = i0 - i2

# Multiply by pi/2 to get the final result
result = (mp.pi / 2) * bessel_diff

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))