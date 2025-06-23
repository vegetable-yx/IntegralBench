import mpmath as mp

# Set internal decimal places to 15 for sufficient precision
mp.dps = 15

# Calculate the inner expression: (sqrt(3) - 1)
numerator = mp.sqrt(3) - 1

# Divide by 2 to get the argument for arcsin
arg = numerator / 2

# Compute arcsin of the argument
arcsin_val = mp.asin(arg)

# Multiply by 2 to get the final result
result = 2 * arcsin_val

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))