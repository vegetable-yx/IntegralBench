import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define the constant multiplier
constant = 506

# Multiply constant by pi
result = constant * mp.pi

# Print result to exactly 10 decimal places
print(mp.nstr(result, n=10))