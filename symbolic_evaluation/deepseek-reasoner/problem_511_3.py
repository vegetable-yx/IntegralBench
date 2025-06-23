import mpmath as mp

# Set internal decimal precision to 15 for accurate calculations
mp.dps = 15

# Calculate the square root of 2
sqrt_2 = mp.sqrt(2)

# Multiply the square root by 2 to get the argument for sine
angle = 2 * sqrt_2

# Calculate the sine of the computed angle
sin_value = mp.sin(angle)

# Multiply the sine result by 2 to get the final answer
result = 2 * sin_value

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))