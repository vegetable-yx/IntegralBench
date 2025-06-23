import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Calculate square root component
sqrt_val = mp.sqrt(2)

# Calculate the argument for sine function
angle = 2 * sqrt_val

# Compute sine of the calculated angle
sin_term = mp.sin(angle)

# Multiply by coefficient to get final result
result = 2 * sin_term

# Print result with 10 decimal places
print(mp.nstr(result, n=10))