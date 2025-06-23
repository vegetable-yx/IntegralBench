import mpmath as mp
mp.dps = 15  # Set internal decimal precision

# Calculate the square root component
sqrt_val = mp.sqrt(2)

# Multiply by 2 to get the angle argument
angle = 2 * sqrt_val

# Compute sine of the calculated angle
sin_angle = mp.sin(angle)

# Multiply by 2 for final result
result = 2 * sin_angle

print(mp.nstr(result, n=10))