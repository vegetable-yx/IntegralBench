import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Compute Bessel function of the first kind of order 0 at x=1
bessel_term = mp.besselj(0, 1)

# Multiply by π to get the final result
result = mp.pi * bessel_term

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))