import mpmath as mp
mp.dps = 15  # Set decimal places for internal calculations

# Calculate the square root component
sqrt_val = mp.sqrt(2)  # Compute square root of 2

# Calculate the angle for sine function
angle = 2 * sqrt_val  # Multiply sqrt(2) by 2

# Compute the sine of the calculated angle
sin_val = mp.sin(angle)  # Calculate sin(2√2)

# Multiply by 2 to get final result
result = 2 * sin_val  # 2 * sin(2√2)

print(mp.nstr(result, n=10))  # Print result with 10 decimal places