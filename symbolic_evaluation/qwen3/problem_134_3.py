import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Calculate square root of 2
sqrt2 = mp.sqrt(2)

# Multiply by pi
result = sqrt2 * mp.pi

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))