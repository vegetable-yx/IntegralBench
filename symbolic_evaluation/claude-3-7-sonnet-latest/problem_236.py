import mpmath as mp

# Set internal precision to 15 decimal places for reliable computation
mp.dps = 15

# Calculate 4 * π
result = 4 * mp.pi

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))