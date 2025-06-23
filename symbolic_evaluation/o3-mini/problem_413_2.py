import mpmath as mp

# Set internal decimal places for sufficient precision
mp.dps = 15

# Define the constant factor
factor = 506

# Multiply the constant by pi
result = factor * mp.pi

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))