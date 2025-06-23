import mpmath as mp

# Set internal decimal precision to 15 for accurate results
mp.dps = 15

# Compute the modified Bessel function of the first kind of order 0 at 6
bessel_value = mp.besseli(0, 6)

# Subtract 1 from the Bessel function value
adjusted_value = bessel_value - 1

# Multiply by pi/3
result = (mp.pi / 3) * adjusted_value

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))