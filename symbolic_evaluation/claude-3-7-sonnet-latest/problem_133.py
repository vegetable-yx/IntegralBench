import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute the modified Bessel function of the first kind of order 0 at z=1
bessel_value = mp.besseli(0, 1)

# Subtract the Bessel function value from 1
result = 1 - bessel_value

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))