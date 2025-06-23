import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the argument for arcsin
sqrt3 = mp.sqrt(3)
numerator = sqrt3 - 1
argument = numerator / 2

# Compute the arcsin value
arcsin_value = mp.asin(argument)

# Multiply by 2 to get final result
result = 2 * arcsin_value

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))