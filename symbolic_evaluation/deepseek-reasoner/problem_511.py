import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate the square root component
sqrt_term = mp.sqrt(2)

# Multiply by 2 for the sine argument
angle = 2 * sqrt_term

# Calculate the sine of the computed value
sin_value = mp.sin(angle)

# Multiply by 2 for the final result
result = 2 * sin_value

print(mp.nstr(result, n=10))