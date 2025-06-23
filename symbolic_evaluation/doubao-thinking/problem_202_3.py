import mpmath as mp

# Set decimal places for internal precision
mp.dps = 15

# Calculate the Bessel function of the first kind of order 1 at 1
bessel_val = mp.besselj(1, 1)

# Multiply by pi to get the result
result = mp.pi * bessel_val

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))