import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the numerator: sqrt(3) - 1
numerator = mp.sqrt(3) - 1

# Compute the argument for arcsin: (sqrt(3) - 1)/2
arg = numerator / 2

# Calculate arcsin of the argument
asin_val = mp.asin(arg)

# Multiply by 2 to get the final result
result = 2 * asin_val

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))