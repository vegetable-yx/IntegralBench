import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Assign pi constant directly from mpmath
result = mp.pi

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))