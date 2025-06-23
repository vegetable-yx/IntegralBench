import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate the numerator sqrt(3) - 1
numerator = mp.sqrt(3) - 1

# Divide by 2 to get the argument for arcsin
arg = numerator / 2

# Compute the arcsin of the argument
arcsin_value = mp.asin(arg)

# Multiply by 2 to get the final result
result = 2 * arcsin_value

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))