import mpmath as mp

# Set the internal precision to 15 decimal places
mp.dps = 15

# Calculate the result: 4 * pi
result = 4 * mp.pi

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))