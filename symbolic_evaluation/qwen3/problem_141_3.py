import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate sinh(1)
sinh_value = mp.sinh(1)

# Square the hyperbolic sine value
result = sinh_value ** 2

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))