import mpmath as mp

# Set internal decimal precision to 15 for intermediate calculations
mp.dps = 15

# Compute the modified Bessel function of the first kind of order 0 at 8
bessel_i0_value = mp.besseli(0, 8)

# Multiply by 2*pi to get the final result
result = 2 * mp.pi * bessel_i0_value

# Print the result rounded to exactly 10 decimal places
print(mp.nstr(result, n=10))