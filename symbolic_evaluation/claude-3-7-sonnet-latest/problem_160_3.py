import mpmath as mp

# Set internal decimal precision to 15 for calculations
mp.dps = 15

# Calculate 2 * π
result = 2 * mp.pi

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))