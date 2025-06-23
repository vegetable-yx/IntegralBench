import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute the square root of 2
sqrt_val = mp.sqrt(2)

# Compute the Bessel function of the first kind of order 1 at sqrt(2)
bessel_val = mp.besselj(1, sqrt_val)

# Multiply by 2 to get the final result
result = 2 * bessel_val

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))