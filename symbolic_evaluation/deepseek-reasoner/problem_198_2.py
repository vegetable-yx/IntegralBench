import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Calculate square root of pi
sqrt_pi = mp.sqrt(mp.pi)

# Multiply by 2 to get final result
result = 2 * sqrt_pi

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))