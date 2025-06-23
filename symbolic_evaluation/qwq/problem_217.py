import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Calculate 2π using mpmath's pi constant
result = 2 * mp.pi

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))