import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Calculate π using mpmath's built-in pi constant
result = mp.pi

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))