import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the Bessel function of the first kind of order 1 at 1
bessel_value = mp.besselj(1, 1)

# Multiply by 2*pi
result = 2 * mp.pi * bessel_value

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))