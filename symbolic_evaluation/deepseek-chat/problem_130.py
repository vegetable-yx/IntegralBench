import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# The analytical expression is 2 * e
# Assign the constant e
e_constant = mp.e

# Multiply by 2 to get the result
result = 2 * e_constant

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))