import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define the constant multiplier
multiplier = 506

# Compute the result: 506 * pi
result = multiplier * mp.pi

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))