import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Calculate the expression: 2 * π
result = 2 * mp.pi

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))