import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate the numerator sqrt(3) - 1
sqrt3 = mp.sqrt(3)
numerator = sqrt3 - 1

# Compute the argument for arcsin
arg = numerator / 2

# Calculate the arcsin value
arcsin_val = mp.asin(arg)

# Multiply by 2 to get the final result
result = 2 * arcsin_val

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))