import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate the numerator (sqrt(3) - 1)
sqrt3 = mp.sqrt(3)
numerator = sqrt3 - 1

# Compute the argument for arcsin function
argument = numerator / 2

# Calculate the arcsin value and multiply by 2
arcsin_value = mp.asin(argument)
result = 2 * arcsin_value

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))