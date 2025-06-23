import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Calculate π squared
pi_squared = mp.pi ** 2

# Subtract 2 from π squared value
result = pi_squared - 2

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))