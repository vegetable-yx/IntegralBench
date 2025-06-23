import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Calculate 4π using mpmath's pi constant
result = 4 * mp.pi

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))