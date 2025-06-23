import mpmath as mp

# Set internal decimal precision to 15 for accurate calculations
mp.dps = 15

# Compute Bessel function of the first kind of order 0 at 1.0
bessel_value = mp.besselj(0, 1.0)

# Multiply by pi to get the final result
result = mp.pi * bessel_value

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))