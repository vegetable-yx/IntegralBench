import mpmath as mp

# Set internal decimal precision to 15 digits
mp.dps = 15

# Calculate 2 * π
result = 2 * mp.pi

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))