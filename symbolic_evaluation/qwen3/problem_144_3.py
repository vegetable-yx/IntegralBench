import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Compute modified Bessel functions of the first kind
I0 = mp.besseli(0, 2)  # I_0(2)
I1 = mp.besseli(1, 2)  # I_1(2)

# Calculate the difference between Bessel functions
bessel_diff = I0 - I1

# Multiply by π/8 to get final result
result = (mp.pi / 8) * bessel_diff

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))