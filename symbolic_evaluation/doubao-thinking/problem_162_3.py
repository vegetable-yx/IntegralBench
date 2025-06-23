import mpmath as mp

# Set internal decimal precision to 15 digits
mp.dps = 15

# Calculate each component of the expression separately
# sqrt(2) component
sqrt_2 = mp.sqrt(2)

# pi component
pi = mp.pi

# Modified Bessel function of the first kind, order 0 at z=1
bessel_i0 = mp.besseli(0, 1)

# Multiply the components: sqrt(2) * pi * I_0(1)
result = sqrt_2 * pi * bessel_i0

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))