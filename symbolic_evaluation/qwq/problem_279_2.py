import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate the modified Bessel function of the first kind of order 0 at 1
bessel_term = mp.besseli(0, 1)

# Multiply by π to get the final result
result = mp.pi * bessel_term

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))