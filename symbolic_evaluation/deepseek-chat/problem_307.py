import mpmath as mp

# Set internal decimal places for high precision calculation
mp.dps = 15

# Assign the constant π to the result variable
result = mp.pi

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))