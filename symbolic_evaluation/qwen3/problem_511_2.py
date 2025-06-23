import mpmath as mp

mp.dps = 15  # Set internal precision

# Calculate square root of 2
sqrt2 = mp.sqrt(2)

# Compute the argument for sine function
angle = 2 * sqrt2

# Calculate sine of the computed angle
sin_value = mp.sin(angle)

# Multiply by 2 for final result
result = 2 * sin_value

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))