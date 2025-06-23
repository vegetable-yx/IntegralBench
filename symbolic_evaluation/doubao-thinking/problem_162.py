import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute the square root of 2
sqrt2 = mp.sqrt(2)

# Compute the value of pi
pi_val = mp.pi

# Compute the modified Bessel function of the first kind of order 0 at 1
bessel_i0_1 = mp.besseli(0, 1)

# Multiply the components: sqrt(2) * pi * I_0(1)
result = sqrt2 * pi_val * bessel_i0_1

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))