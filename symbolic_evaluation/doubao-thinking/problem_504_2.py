import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Define the input value x (example value, adjust as needed)
x = mp.pi / 4  # Example evaluation at x = π/4

# Calculate sin(x) and raise it to the 100th power
sin_x = mp.sin(x)
sin_power = sin_x**100

# Calculate sin(100x)
sin_100x = mp.sin(100 * x)

# Combine components for final result
numerator = sin_power * sin_100x
result = numerator / 100

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))