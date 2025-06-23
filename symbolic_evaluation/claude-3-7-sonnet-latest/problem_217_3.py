import mpmath as mp

# Set internal decimal precision to 15 for intermediate calculations
mp.dps = 15

# Compute Bessel function of the first kind of order 0 at z=1
bessel_value = mp.besselj(0, 1)

# Multiply by pi/2 to get the final result
result = (mp.pi / 2) * bessel_value

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))