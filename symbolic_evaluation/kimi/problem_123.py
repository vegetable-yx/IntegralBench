import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Calculate π using mpmath's built-in constant
result = mp.pi

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))