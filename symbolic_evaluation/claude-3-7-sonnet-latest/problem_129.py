import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate pi * sqrt(2)
pi_sqrt2 = mp.pi * mp.sqrt(2)

# Calculate the modified Bessel function of the first kind, order 0 at 1
bessel_i0 = mp.besseli(0, 1)

# Multiply the two components
result = pi_sqrt2 * bessel_i0

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))