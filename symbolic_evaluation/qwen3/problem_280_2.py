import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate 3^(1/4) using power function
three_power = mp.power(3, 0.25)

# Calculate hyperbolic sine of 3
sinh_value = mp.sinh(3)

# Multiply components together
result = 2 * three_power * sinh_value

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))