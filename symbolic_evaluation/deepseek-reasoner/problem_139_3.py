import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate hyperbolic sine of 1
sinh_value = mp.sinh(1)

# Square the hyperbolic sine result
sinh_squared = sinh_value ** 2

# Multiply by 2 to get the final result
result = 2 * sinh_squared

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))