import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Calculate 6π using mpmath's high-precision pi constant
result = 6 * mp.pi

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))