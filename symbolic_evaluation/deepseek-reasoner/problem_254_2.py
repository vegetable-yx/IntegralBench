import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate -3π directly using mpmath's pi constant
result = -3 * mp.pi

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))