import mpmath as mp

# Set decimal places for internal calculations
mp.dps = 15

# Compute the modified Bessel function of the first kind, order 0 at 2
bessel_i0 = mp.besseli(0, 2)

# Subtract 1 from the Bessel function result
bessel_diff = bessel_i0 - 1

# Multiply by pi/2 to get the final result
result = (mp.pi / 2) * bessel_diff

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))