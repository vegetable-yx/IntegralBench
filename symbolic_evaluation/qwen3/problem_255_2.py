import mpmath as mp
mp.dps = 15  # Set decimal places for internal calculations

# Calculate -3π using mpmath's pi constant
result = -3 * mp.pi

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))