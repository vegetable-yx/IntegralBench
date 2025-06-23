import mpmath as mp

# Set internal decimal places for high precision
mp.mp.dps = 15

# Calculate the square root of 2
sqrt2 = mp.sqrt(2)

# Multiply by 3
three_sqrt2 = 3 * sqrt2

# Multiply by pi
product = three_sqrt2 * mp.pi

# Apply the negative sign
result = -product

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))