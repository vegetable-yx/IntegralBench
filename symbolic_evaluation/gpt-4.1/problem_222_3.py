import mpmath as mp

# Set internal decimal places to 15 for sufficient precision
mp.dps = 15

# Calculate 3 * π
result = 3 * mp.pi

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))