import mpmath as mp

# Set precision to 15 decimal places for intermediate calculations
mp.dps = 15

# Calculate modified Bessel functions of the first kind
I0 = mp.besseli(0, 1)  # I_0(1)
I2 = mp.besseli(2, 1)  # I_2(1)

# Compute the difference between Bessel functions
bessel_diff = I0 - I2

# Multiply by π/2 to get final result
result = (mp.pi / 2) * bessel_diff

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))