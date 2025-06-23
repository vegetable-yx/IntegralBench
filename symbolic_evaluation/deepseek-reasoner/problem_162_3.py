import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate components of the expression
sqrt_2 = mp.sqrt(2)  # Square root of 2
pi = mp.pi           # Pi constant
bessel_i0_1 = mp.besseli(0, 1)  # Modified Bessel function of first kind, order 0 at 1

# Combine components to get final result
result = sqrt_2 * pi * bessel_i0_1

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))