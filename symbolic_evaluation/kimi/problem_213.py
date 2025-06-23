import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Compute the Bessel function of the first kind of order 0 at 1
bessel_j0 = mp.besselj(0, 1)

# Multiply by π to get the final result
result = mp.pi * bessel_j0

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))