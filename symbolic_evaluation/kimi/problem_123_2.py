import mpmath as mp
mp.dps = 15  # Set decimal places for internal calculations

# Calculate π using mpmath's built-in constant
result = mp.pi

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))