import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute the Bessel function of the first kind of order 0 at 1
bessel_value = mp.besselj(0, 1)

# Multiply by π to get the final result
result = mp.pi * bessel_value

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))