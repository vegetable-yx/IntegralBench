import mpmath as mp

# Set internal decimal places for high precision
mp.dps = 15

# Calculate the Bessel function of the first kind of order 0 at 1
bessel_value = mp.besselj(0, 1)

# Multiply by pi to get the final result
result = mp.pi * bessel_value

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))