import mpmath as mp

# Set internal decimal places to 15 for sufficient precision
mp.dps = 15

# Calculate the value of pi
pi_val = mp.pi

# Calculate the square root of 2
sqrt2 = mp.sqrt(2)

# Compute the modified Bessel function of the first kind of order 1 at 1
bessel_val = mp.besseli(1, 1)

# Multiply the components: π * √2 * I_1(1)
result = pi_val * sqrt2 * bessel_val

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))