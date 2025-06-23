import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate hyperbolic sine of 1
sinh_1 = mp.sinh(1)

# Square the hyperbolic sine value
sinh_squared = sinh_1 ** 2

# Multiply by 4 to get the final result
result = 4 * sinh_squared

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))