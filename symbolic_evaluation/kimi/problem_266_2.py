import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Compute the Bessel function of the first kind of order 0 at 2
bessel_value = mp.besselj(0, 2)

# Multiply by pi/2
result = (mp.pi / 2) * bessel_value

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))