import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute the modified Bessel function of the first kind of order 2 at 1.0
bessel_val = mp.besseli(2, 1.0)

# Multiply the result by 2
result = 2 * bessel_val

# Print the final result to 10 decimal places
print(mp.nstr(result, n=10))