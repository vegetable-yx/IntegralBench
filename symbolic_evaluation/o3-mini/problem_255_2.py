import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate -3 * π directly
result = -3 * mp.pi

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))