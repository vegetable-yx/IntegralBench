import mpmath as mp

mp.dps = 15  # Set internal precision

# Calculate sqrt(2) component
sqrt_2 = mp.sqrt(2)

# Multiply by 3
three_sqrt_2 = 3 * sqrt_2

# Multiply by pi
result = -three_sqrt_2 * mp.pi

# Print result with 10 decimal places
print(mp.nstr(result, n=10))