import mpmath as mp

# Set the internal precision to 15 decimal places
mp.dps = 15

# Calculate the result: 506 times π
result = 506 * mp.pi

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))