import mpmath as mp

# Set internal precision to 15 decimal places for reliable calculation
mp.dps = 15

# Calculate the analytical expression: (3 * π) / 4
pi = mp.pi  # Get the precise value of π
numerator = 3 * pi  # Multiply π by 3
result = numerator / 4  # Divide by 4 to get the final value

# Print the result formatted to 10 decimal places
print(mp.nstr(result, n=10))