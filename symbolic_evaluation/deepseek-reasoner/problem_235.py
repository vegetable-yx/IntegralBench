import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate 2π using mpmath's pi constant
result = 2 * mp.pi

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))