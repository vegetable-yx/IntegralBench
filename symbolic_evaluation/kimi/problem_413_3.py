import mpmath as mp

# Set the internal decimal precision to 15 for accurate calculations
mp.dps = 15

# Define the constant multiplier
constant = 506

# Multiply the constant by pi
result = constant * mp.pi

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))