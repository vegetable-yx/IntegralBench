import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate the square root of 2
sqrt2 = mp.sqrt(2)

# Multiply by 2 to get the argument for sine function
angle = 2 * sqrt2

# Calculate sine of the computed angle
sin_value = mp.sin(angle)

# Multiply by 2 to get the final result
result = 2 * sin_value

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))