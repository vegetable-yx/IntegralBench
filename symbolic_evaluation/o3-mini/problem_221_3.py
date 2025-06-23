import mpmath as mp

# Set internal decimal places for precision
mp.dps = 15

# Define the analytical expression: (3 * pi) / 16
# Step 1: Multiply 3 by pi
numerator = 3 * mp.pi

# Step 2: Divide the numerator by 16
result = numerator / 16

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))