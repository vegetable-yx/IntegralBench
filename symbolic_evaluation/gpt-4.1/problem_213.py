import mpmath as mp

# Set internal precision to 15 decimal places for accuracy
mp.dps = 15

# Compute the Bessel function of the first kind of order 1 at 1
bessel_value = mp.besselj(1, 1)

# Multiply by π to get the final result
result = mp.pi * bessel_value

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))