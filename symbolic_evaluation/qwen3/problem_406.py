import mpmath as mp
mp.dps = 15

# Calculate the numerator: sqrt(3) - 1
numerator = mp.sqrt(3) - 1

# Compute the argument for arcsin function
argument = numerator / 2

# Calculate the arcsin of the argument
arcsin_value = mp.asin(argument)

# Multiply by 2 to get the final result
result = 2 * arcsin_value

print(mp.nstr(result, n=10))