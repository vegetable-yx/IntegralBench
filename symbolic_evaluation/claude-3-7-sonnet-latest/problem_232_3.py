import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate 2 * π
result = 2 * mp.pi

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))