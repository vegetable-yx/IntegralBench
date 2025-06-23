import mpmath as mp

# Set internal decimal places for precision
mp.dps = 15

# Calculate sqrt(2) to high precision
sqrt2 = mp.sqrt(2)

# Multiply sqrt(2) by 4
four_sqrt2 = 4 * sqrt2

# Subtract 1 from the result
numerator_part = four_sqrt2 - 1

# Multiply by pi
numerator = mp.pi * numerator_part

# Divide by 4 to get the final result
result = numerator / 4

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))