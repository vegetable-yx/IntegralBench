import mpmath as mp

# Set internal precision to 15 decimal places for accurate computation
mp.dps = 15

# Define the constant factor from the analytical expression
constant_factor = -3

# Multiply the constant by pi to compute the result
result = constant_factor * mp.pi

# Print the result formatted to 10 decimal places
print(mp.nstr(result, n=10))