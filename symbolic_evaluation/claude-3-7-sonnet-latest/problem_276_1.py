import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the modified Bessel function of the first kind, order 0 at 6
bessel_term = mp.besseli(0, 6)

# Multiply by 2*pi
result = 2 * mp.pi * bessel_term

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))