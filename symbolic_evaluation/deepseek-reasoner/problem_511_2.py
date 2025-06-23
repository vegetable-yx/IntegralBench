import mpmath as mp

# Set precision to 15 decimal places for intermediate calculations
mp.dps = 15

# Calculate square root of 2
sqrt_two = mp.sqrt(2)

# Calculate the angle argument for sine function
angle = 2 * sqrt_two

# Compute sine of the calculated angle
sin_value = mp.sin(angle)

# Multiply by 2 to get final result
result = 2 * sin_value

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))