import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Calculate -3π directly using mpmath's pi constant
result = -3 * mp.pi

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))