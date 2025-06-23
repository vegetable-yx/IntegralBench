import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the square root of 3
sqrt3 = mp.sqrt(3)

# Multiply by the constant 7
numerator_part = 7 * sqrt3

# Multiply by pi
numerator = numerator_part * mp.pi

# Divide by 9 to get the final result
result = numerator / 9

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))