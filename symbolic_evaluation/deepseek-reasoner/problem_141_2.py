import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate sinh(1)
sinh_1 = mp.sinh(1)

# Square the hyperbolic sine result
result = sinh_1 ** 2

# Print the final result with 10 decimal places precision
print(mp.nstr(result, n=10))