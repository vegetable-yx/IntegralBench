import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the square root of 2
sqrt_two = mp.sqrt(2)

# Get the constant pi
pi_val = mp.pi

# Compute the modified Bessel function of the first kind of order 0 at 1
bessel_i0 = mp.besseli(0, 1)

# Multiply the components: sqrt(2) * pi * I_0(1)
result = sqrt_two * pi_val * bessel_i0

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))