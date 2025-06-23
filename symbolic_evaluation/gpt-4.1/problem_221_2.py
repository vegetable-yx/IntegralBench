import mpmath as mp

# Set internal decimal precision to 15 digits for accurate calculations
mp.dps = 15

# Calculate the numerator: 3 * π
numerator = 3 * mp.pi

# Divide the numerator by 16 to get the final result
result = numerator / 16

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))