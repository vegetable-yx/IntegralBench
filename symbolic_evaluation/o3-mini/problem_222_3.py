import mpmath as mp

# Set internal precision to 15 decimal places for accurate computation
mp.dps = 15

# Define the constant factor
factor = 3

# Multiply the constant factor by pi
result = factor * mp.pi

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))