import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Calculate π/4 directly using mpmath's constant
result = mp.pi / 4

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))