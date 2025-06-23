import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate square root of 2
sqrt_2 = mp.sqrt(2)

# Compute Bessel function of the first kind of order 2 at sqrt(2)
bessel_j2 = mp.besselj(2, sqrt_2)

# Multiply by 2π to get final result
result = 2 * mp.pi * bessel_j2

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))