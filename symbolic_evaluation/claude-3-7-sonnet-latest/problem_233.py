import mpmath as mp

# Set internal decimal precision to 15 for accurate calculations
mp.dps = 15

# Calculate 4 times pi
result = 4 * mp.pi

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))