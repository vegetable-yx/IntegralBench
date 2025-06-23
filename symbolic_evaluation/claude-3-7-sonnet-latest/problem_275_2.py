import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the square root of 3
sqrt3 = mp.sqrt(3)

# Compute the constant factor (3 * sqrt(3)) / 2
constant_factor = (3 * sqrt3) / 2

# Calculate hyperbolic sine of 3
sinh_val = mp.sinh(3)

# Multiply constant factor by sinh(3) to get the result
result = constant_factor * sinh_val

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))