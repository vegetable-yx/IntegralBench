import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the values of the modified Bessel functions
# I_0(5) - modified Bessel function of the first kind, order 0 at 5
bessel_i0 = mp.besseli(0, 5)
# I_2(5) - modified Bessel function of the first kind, order 2 at 5
bessel_i2 = mp.besseli(2, 5)

# Sum the Bessel function values
bessel_sum = bessel_i0 + bessel_i2

# Compute the constant factor: 125 / 4
constant_factor = mp.mpf(125) / 4

# Multiply by pi and the constant factor
result = constant_factor * mp.pi * bessel_sum

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))