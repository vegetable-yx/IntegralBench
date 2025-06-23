import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute the modified Bessel function of the first kind of order 0 at 6
I0 = mp.besseli(0, 6)

# Subtract 1 from the Bessel function result
bessel_term = I0 - 1

# Multiply by pi/6 to get the final result
result = (mp.pi / 6) * bessel_term

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))