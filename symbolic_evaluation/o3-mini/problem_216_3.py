import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute the constant factor: pi * sqrt(2)
factor = mp.pi * mp.sqrt(2)

# Compute the Bessel function of the first kind of order 0 at 2
bessel_value = mp.besselj(0, 2)

# Multiply to get the result
result = factor * bessel_value

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))